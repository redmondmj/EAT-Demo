# EAT-Demo
NSCC Demo for École acadienne de Truro

# École acadienne de Truro Live Demo | Bienvenue

If needed run the [Setup](setup.md)

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
* [Google Dorking](https://github.com/chr3st5an/Google-Dorking) Demo
    1. `allintext: "DVWA" "username" "password"`
    2. `allintext:"DVWA" filetype:pdf`
    3. 
* Identify a Target
  * We'll just create our own!
    * `docker run --rm -it -p 80:80 vulnerables/web-dvwa`
    * Just Browsing http://localhost
    * Click **Login** and then click **Create/Reset Database**. 


### Step 2 | Attack (20Min)
* Browser based attacks
    1. Command Injection \
    `127.0.0.1; ls -la /` \
    `127.0.0.1 ; cat /etc/passwd | tee /tmp/passwd`
    2. SQL Injection \
    `1' OR '1'='1'#` \
    `%' and 1=0 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #`
* Advanced Attacks (Automation Demo) \
  * Password Brute Force
    * Let's use brute.py
    * We'll specify our target. (Line 53)
    * We need to know usernames (line 48)
    * We need a dictionary of common passwords. (line 113) \
    `./brute.py`



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

