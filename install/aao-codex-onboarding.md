# Getting started with Codex at AAO

This guide takes a new AAO user from a fresh computer to a working Codex project with AAO skills, version control, Office integration, and a first automation project.

Allow 60–90 minutes for the basic setup. GitLab access and Microsoft 365 add-ins may take longer if an administrator or the AAO helpdesk must approve them.

## Before you begin

You will need:

- an AAO or Macquarie email account;
- permission to install applications on the computer;
- a budget owner who can approve an OpenAI plan or usage credits;
- access to the AAO helpdesk; and
- one concrete, repetitive task that you would like to improve.

Keep public and internal material separate:

- `AAO-skills` is for broadly shareable material;
- AAO project code and internal working material belong in the approved AAO GitLab project; and
- restricted, partner-private, Defence-adjacent, commercially sensitive, controlled, or clearance-dependent material must not be copied into the public skills repository or an unapproved AI service.

Do not paste passwords, private SSH keys, recovery codes, or multi-factor authentication codes into a Codex conversation. Enter credentials only in the relevant sign-in page.

## Completion checklist

- [ ] Choose a ChatGPT plan and/or Codex credit budget suitable for regular agent work.
- [ ] Install Codex and sign in.
- [ ] Install and configure Git; optionally install TortoiseGit on Windows.
- [ ] Review Codex permissions and enable Computer Use where appropriate.
- [ ] Install the official Codex Chrome extension if existing Chrome sessions are needed.
- [ ] Create or confirm a GitHub account, enable two-factor authentication, and configure SSH.
- [ ] Clone and install the public `AAO-skills` repository.
- [ ] Schedule the weekly AAO skills update automation.
- [ ] Inventory the approved parts of OneDrive and create reviewed folder indexes.
- [ ] Install approved first-party OpenAI add-ins for Microsoft Office.
- [ ] Obtain AAO GitLab access and request an internal project repository.
- [ ] Open the internal project folder in Codex.
- [ ] Start with one bounded automation of a real time sink.

## 1. Choose a plan and usage budget

Codex is available through eligible ChatGPT plans, with additional usage credits available on supported plans. Prices, included limits, and credit rules change, so check the [current ChatGPT pricing](https://openai.com/chatgpt/pricing/) and [Codex credit guidance](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-pluspro) when purchasing.

The AAO setup walkthrough on 4 August 2026 compared lower-cost and higher-volume options. The practical point was that light plans may reach their included agent limits quickly during sustained work. The dollar amounts discussed in that session were examples, not an AAO policy or a guaranteed current price.

Agree on:

- who pays;
- the initial monthly limit;
- whether automatic credit top-up is allowed; and
- when usage and value will be reviewed.

## 2. Install Codex

Download Codex only from OpenAI's [Codex getting-started page](https://openai.com/codex/get-started/) or another official OpenAI page. It is available on macOS and Windows.

After installation:

1. Sign in with the approved ChatGPT account.
2. Open a harmless test folder.
3. Ask: `Tell me which folder you can access. Do not change any files.`
4. Confirm that the answer names only the intended folder.

## 3. Set up Git

Git records changes to text, scripts, configuration, and documentation. TortoiseGit is an optional Windows interface that adds visible status icons and right-click actions; Git for Windows is still required underneath it.

### Windows prompt

```text
Check whether Git for Windows is installed. If it is missing, install it using
the standard recommended settings for this computer. Then install TortoiseGit
if it is not already installed. Configure my Git name and AAO email only after
asking me for their exact values. Verify the installation and explain the
result in plain language. Do not create or change a repository yet.
```

Restart Windows Explorer or the computer if the installer requires it.

### macOS prompt

```text
Check whether Git works on this Mac. If it is missing, help me install the
Apple command-line tools or another appropriate Git package. Configure my Git
name and AAO email only after asking me for their exact values. Verify the
installation and explain the result in plain language. Do not create or change
a repository yet.
```

The success check is a working Git version plus the correct name and email. Do not use a colleague's identity or a guessed email address.

## 4. Review permissions and enable Computer Use

Codex normally begins with constrained access. Some AAO workflows also need it to launch and operate desktop applications.

1. In Codex settings, review file, command, network, browser, and Computer Use permissions.
2. Enable Computer Use if the planned task needs desktop applications.
3. Grant broader or full access only on an approved computer and only after checking the folder, accounts, and data in scope.
4. Keep confirmation enabled for sending, publishing, deleting, purchasing, or changing access.
5. Test Computer Use with a reversible task, such as opening an application and reporting its name without editing a file.

Full access is powerful, not a substitute for scope. A useful task still says what Codex may inspect, what it may change, and what requires confirmation.

## 5. Connect a browser

Codex has a built-in browser. Install the official Codex Chrome extension only when a task needs an existing Chrome profile, signed-in session, open tabs, or other Chrome extensions. Start from OpenAI's [browser guidance](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app) rather than searching the Chrome store by name, where lookalike extensions may appear.

After installation:

1. Check that the publisher is OpenAI.
2. Open a public test page in Chrome.
3. Ask Codex to identify the page title without navigating away.
4. Review the active browser profile before allowing work on a signed-in service.

## 6. Set up GitHub and SSH

The public AAO skills repository is hosted on GitHub. A person must complete account sign-in, email verification, multi-factor authentication, CAPTCHA, recovery-code storage, and any organisation invitation. Codex can inspect the computer, generate an SSH key pair, upload the **public** key after approval, and test the connection.

Use this prompt:

```text
Help me set up GitHub access for this computer.

1. Check for existing SSH keys without displaying any private key.
2. If a suitable key does not exist, create a modern SSH key for GitHub using
   my confirmed AAO email as its label.
3. Show me the public-key fingerprint and where the private key is stored.
4. Help me create or sign in to my GitHub account, but pause for me to enter
   credentials, verify email, complete MFA, or accept an organisation invite.
5. Add only the public key to GitHub after I approve it.
6. Test SSH access and report the GitHub username that answered.

Never display, upload, or copy the private key into chat.
```

GitHub's official documentation covers [account creation](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) and [adding an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). Enable two-factor authentication and store recovery codes in the approved password manager.

## 7. Clone and install AAO skills

The canonical public repository is:

```text
git@github.com:Macquarie-Astronomical-Adaptive-Optics/AAO-skills.git
```

Open a parent folder where you keep AAO development work, then ask:

```text
Clone the public AAO-skills repository from
git@github.com:Macquarie-Astronomical-Adaptive-Optics/AAO-skills.git into an
AAO-skills folder. Confirm that the remote is correct. Read its README and use
the repository's own installer to install its skills for Codex and Claude Code
on this operating system. Do not overwrite unrelated existing skill folders.
Report every installed skill and any collision or error.
```

The repository installers are:

- macOS or Linux: `./install/install-agent-skills.sh`
- Windows: `powershell.exe -ExecutionPolicy Bypass -File .\install\install-agent-skills.ps1`

On macOS and Linux, installed entries link to the canonical repository. On Windows, the installer creates marked copies and must be rerun after an update. Running the installer after every update on all platforms also links or copies newly added skills.

Success means that Codex can list the AAO skills and identify this repository as their source.

## 8. Schedule the weekly skills update

Ask Codex to create a recurring automation. Choose a time when the computer is normally on and connected—for example, Monday at 9:00 am local time.

```text
Create a recurring automation named "Update AAO skills" that runs every Monday
at 9:00 am local time.

Its job is to update my local AAO-skills checkout and install any new or changed
skills. Each run must:

1. Locate the checkout whose origin is
   git@github.com:Macquarie-Astronomical-Adaptive-Optics/AAO-skills.git.
2. Record the current branch and commit, and check for modified, staged,
   untracked, or conflicted files.
3. If the checkout is not clean, is not on main, or has diverged from
   origin/main, stop without changing anything and report the problem.
4. Run `git pull --ff-only origin main` to update main. Never reset, clean,
   rebase, force, delete, or discard local work.
5. Run the repository's install-agent-skills script for this operating system.
6. Verify the installed AAO skill names against the skill folders in the
   repository.
7. Report the old and new commit IDs, newly added or removed skills, installer
   collisions, and any error. If nothing changed, say so briefly.

Do not update any other repository and do not publish or push anything.
```

After creating it, inspect the displayed schedule and run it once manually. A successful test either reports a clean no-change result or a fast-forward update followed by a successful installation.

## 9. Create a reviewed OneDrive index

Open only the approved OneDrive folder with **Open Folder**. A recursive scan can hydrate cloud-only files and may encounter confidential material, so begin with a read-only inventory and review the proposed scope before creating index files.

First prompt:

```text
Read this OneDrive folder recursively to prepare an index plan. Do not create,
edit, move, rename, or delete anything yet. List the major folders, the broad
kinds of files in each, obvious date ranges, inaccessible areas, existing
indexes, and folders that may need a privacy or information-control decision.
Do not reproduce sensitive file contents. Propose which major folders should
receive an INDEX.md file, then wait for my approval.
```

After reviewing the inventory, use:

```text
Create the approved INDEX.md files only. Each index should describe the folder's
purpose, main subfolders, file types, date range, and a small set of useful
entry points, with relative links where practical. Preserve existing indexes
unless I explicitly approve an update. Mark uncertain descriptions as
uncertain. Skip hidden, system, temporary, sync-conflict, and excluded folders.
Finish with a list of every file created or changed.
```

Review the generated indexes before relying on them. An index is a navigation aid, not proof that every file was read correctly or is current.

## 10. Add Microsoft Office integration

Use first-party add-ins only, and check the publisher before installation. Availability may depend on the Microsoft 365 tenant, ChatGPT plan, workspace role, and administrator settings.

- **Excel:** install ChatGPT from **Home → Add-ins**, sign in, and follow the official [ChatGPT for Excel](https://help.openai.com/en/articles/20001063-chatgpt-for-excel) guide.
- **PowerPoint:** install ChatGPT from **Home → Add-ins**, sign in, and follow the official [ChatGPT for PowerPoint](https://help.openai.com/en/articles/20001242-chatgpt-for-powerpoint) guide.
- **Word:** search the Microsoft Marketplace from Word and install only an entry whose publisher and support page confirm that it is from OpenAI. As of 4 August 2026, the public OpenAI documentation checked for this guide clearly documents Excel and PowerPoint add-ins but not a first-party Word add-in. Do not substitute an unofficial lookalike; ask the Microsoft 365 administrator or use Codex to work with a copied `.docx` file instead.

Test each approved add-in on a disposable file. Keep the original file, ask for one small change, inspect the result, and only then use it on working material.

## 11. Obtain AAO GitLab access

AAO internal programming work should use the approved GitLab service rather than the public skills repository.

1. Create or confirm the required account at [Data Central](https://datacentral.org.au/).
2. Try the AAO development service at `https://dev.datacentral.org.au/`. It may require an approved account, internal access, or helpdesk action.
3. Ask the AAO helpdesk for GitLab access if it is not already present.
4. Ask the helpdesk to create a project for the team's Codex-assisted programming work unless an appropriate project already exists. Include the team, project purpose, intended members, and proposed project name.
5. Use the clone address shown by that GitLab project; do not guess it from the web address.

After the account and project exist, ask Codex:

```text
Set up SSH access to the approved AAO GitLab service on this computer. Inspect
the existing SSH configuration first. Create a separate modern key if that is
safer than reusing another service's key, and never display the private key.
Pause for me to complete sign-in or MFA. Add only the public key after I approve
it, test the connection, and report which GitLab account answered.
```

In the 4 August setup walkthrough, the user could reach Data Central but project creation appeared to be restricted and a helpdesk request was submitted. Treat the helpdesk step as expected, not as a setup failure.

## 12. Create or clone the internal project

If the GitLab repository is ready, clone it into an approved AAO working location and confirm that its remote points to the internal GitLab project.

If project creation is delayed, use a local repository temporarily:

```text
Create a local Git repository for this AAO project. Add a short README describing
its purpose and a TODO stating that the repository must be connected to the
approved AAO GitLab project when the helpdesk supplies it. Do not add a public
GitHub remote. Add an appropriate ignore file, make an initial status report,
and ask before committing anything.
```

Do not place the temporary repository inside OneDrive if sync behaviour could interfere with Git. Do not treat a local repository as backed up until the GitLab remote is connected and a push has been verified.

## 13. Open the project in Codex

Use **Open Folder** and select the project repository, not all of OneDrive or the whole user profile.

Ask Codex to begin with a read-only orientation:

```text
Read this project without changing it. Summarise its purpose, structure,
instructions, current Git status, tests, and TODO items. Identify anything that
looks sensitive or unclear before proposing work.
```

Check that Codex identifies the correct repository and internal remote.

## 14. Automate the biggest time sink

Describe the work in ordinary language: what arrives, what you do, which applications and files are involved, what judgement is required, what a good result looks like, and which mistakes would matter.

Use this starting prompt:

```text
My largest repetitive time sink is: [describe it].

First map the current workflow, inputs, outputs, decision points, failure modes,
data restrictions, and human approvals. Then propose the smallest useful part
we can automate and a test using a disposable or copied example. Do not operate
on live project data until I approve the plan. Keep engineering judgement and
release approval with a named person.
```

Prefer a bounded semi-automated workflow with a visible test and human review. A plausible output is not an accepted engineering result.

## Suggested next skill: `set-up-everything-else`

A future onboarding skill could automate the repeatable parts of this guide:

- detect the operating system and existing tools;
- verify Git and offer TortoiseGit on Windows;
- test Codex permissions without broadening them silently;
- guide the human through account, MFA, and administrator handoffs;
- clone and install `AAO-skills`;
- create and test the weekly update automation;
- prepare a read-only OneDrive inventory;
- check first-party Office add-in availability;
- prepare the GitLab helpdesk request; and
- create a local project with a clear GitLab TODO when access is delayed.

The skill should never handle passwords, bypass approvals, upload private keys, place internal work in a public repository, or claim that account creation, access, backup, installation, or an automation succeeded without checking it.

## Evidence and maintenance note

The workflow was cross-checked against the automated, uncorrected transcript of the AAO setup session with Zhemin Cai on 4 August 2026. That session directly covered plan limits, Codex installation, Git for Windows and TortoiseGit, GitHub and SSH, AAO skills installation, OneDrive indexing, Computer Use, Chrome, Excel integration, Data Central/GitLab access, an internal project, and a first engineering automation. Product behaviour, prices, and institutional access paths can change; the linked first-party documentation and AAO helpdesk are authoritative for the current setup.
