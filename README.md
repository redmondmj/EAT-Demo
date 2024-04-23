# EAT-Demo
NSCC Demo for École acadienne de Truro

# École acadienne de Truro Live Demo | Bienvenue

## Setup
1. Launch Terminal/Powershell as Administrator (right click Start Button)
2. Update WSL `wsl --update` or [Install](https://learn.microsoft.com/en-us/windows/wsl/install)
3. Install Git `winget install git.git`
4. Install Docker `winget install Docker.DockerDesktop`
5. Launch Docker
6. Restart PS (As Admin)
7. Pull the DVWA Image `docker pull vulnerables/web-dvwa`
8. Brute Force?
    1. `winget install python3` (if needed)
    2. `pip install requests bs4`
8. Clone the Repo 

## Part 1 | Web Hacking
### Security Intro (Obligitory Boring Stuff)  (10 Min)
* Ethical Hacking
  * Always get permission
  * Hacking is just applied Skills/Knowledge (Creatively!)
* Staying Safe
  * Stong Passwords \
    https://haveibeenpwned.com/
  * Multi-Factor
  * Always update

### Step 1 | Recon (15 Min)
* Google Dorking Demo
    1. `allintext: "DVWA" "username" "password"`
    2. `allintext:"DVWA" filetype:pdf`
    3. 
* Identify a Target
    * We'll create our own! \
    `docker run --rm -it -p 80:80 vulnerables/web-dvwa`
* Just Browsing http://localhost
* Vulnerbility Scanning (just an exmaple)
     * ZAP Screenshot

### Step 2 | Attack (20Min)
* Browser based attacks
    1. Command Injection \
    `127.0.0.1; ls -la /`
    2. SQL Injection \
    `1' OR '1'='1'#`
    3. XSS (Reflected)
* Advanced Attacks (Automation Demo) \
  https://github.com/In3tinct/DVWA-Automation



## Part 2 | Generative AI - DYI ChatBot

### What is AI? (More Obligitory Boring Stuff) (5 Min)
 * How does AI learn?
 * How can we control it?
   * Data Sets
   * decision Trees
   * HardCoded!

### Botpress Demo (30 Min)
* Creating a simple Flow
* Set up a variable
* Load some data
* Add some Guardrails!
* Test your bot!

