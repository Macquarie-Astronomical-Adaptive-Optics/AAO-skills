param(
    [string]$CodexSkillsDir = $env:AAO_CODEX_SKILLS_DIR,
    [string]$ClaudeSkillsDir = $env:AAO_CLAUDE_SKILLS_DIR
)

$ErrorActionPreference = "Stop"

$AaoRepositoryRoot = Split-Path -Parent $PSScriptRoot
$AaoSkillsSource = Join-Path $AaoRepositoryRoot "plugins\aao-skills\skills"
$AaoUserProfile = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::UserProfile)
$AaoManagedMarker = ".aao-skills-managed"

if ([string]::IsNullOrWhiteSpace($CodexSkillsDir)) {
    $CodexSkillsDir = Join-Path $AaoUserProfile ".agents\skills"
}
if ([string]::IsNullOrWhiteSpace($ClaudeSkillsDir)) {
    $ClaudeSkillsDir = Join-Path $AaoUserProfile ".claude\skills"
}

function Install-AaoSkillCopies {
    param(
        [string]$Product,
        [string]$Destination
    )

    New-Item -ItemType Directory -Force -Path $Destination | Out-Null

    foreach ($Skill in (Get-ChildItem -LiteralPath $AaoSkillsSource -Directory)) {
        $SkillSource = $Skill.FullName
        $SkillName = $Skill.Name
        $SkillEntryPoint = Join-Path $SkillSource "SKILL.md"
        if (-not (Test-Path -LiteralPath $SkillEntryPoint -PathType Leaf)) {
            continue
        }

        $SkillDestination = Join-Path $Destination $SkillName
        $MarkerPath = Join-Path $SkillDestination $AaoManagedMarker

        if (Test-Path -LiteralPath $SkillDestination) {
            if (-not (Test-Path -LiteralPath $MarkerPath -PathType Leaf)) {
                Write-Warning "Skipped $SkillName for ${Product}: $SkillDestination exists and is not installer-managed."
                continue
            }
            Remove-Item -LiteralPath $SkillDestination -Recurse -Force
        }

        Copy-Item -LiteralPath $SkillSource -Destination $SkillDestination -Recurse
        Set-Content -LiteralPath (Join-Path $SkillDestination $AaoManagedMarker) -Encoding UTF8 -Value @(
            "Managed copy created by AAO-skills/install/install-agent-skills.ps1",
            "Canonical source: $SkillSource",
            "Refresh by rerunning the installer; do not edit this installed copy."
        )
    }

    Write-Host "Installed AAO skill copies for $Product in $Destination"
}

Install-AaoSkillCopies -Product "Codex" -Destination $CodexSkillsDir
Install-AaoSkillCopies -Product "Claude Code" -Destination $ClaudeSkillsDir

Write-Host "Windows installations are generated from the one canonical tree at $AaoSkillsSource"
