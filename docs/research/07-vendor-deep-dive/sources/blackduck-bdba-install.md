# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/3we1j4a_j1FLyNb0zozX4g
# Reader base: https://docs.blackduck.com/r/bdba-installation/2026.9.0/
# Captured: 2026-09-21



===== TOPIC: Black Duck Binary Analysis Overview =====
# URL: https://docs.blackduck.com/r/bdba-installation/2026.9.0/ (topic id 26~K176NOsSyXrrt_V3mHg)

Black Duck Binary Analysis is a software composition analysis (SCA) scanner for compiled
            code.

    

    Problems Solved

        
        
            Here's what it can do for you:

            
                Provides a clear view of risk. Black Duck Binary Analysis gives unmatched
                    visibility into open source and third-party code in applications and containers.
                    Black Duck Binary Analysis gives you the information you need to verify that
                    your product has exactly the components you expect, that those components are up
                    to date, and that no inappropriate software licenses have been used. It creates
                    a high-level overview of the composition and overall health of software,
                    including desktop and mobile applications, embedded system firmware, and more.
                    Better visibility leads to better decisions regarding mergers and acquisitions,
                    as well.

                Helps to manage the risk. Black Duck Binary Analysis provides a comprehensive
                    solution for managing security, quality, and license compliance risk.

                Informs your decisions about software consumption. Reduce security risks and the
                    threat of license noncompliance. Identify known open source vulnerabilities,
                    licensing obligations, sources of sensitive data leakage, and application
                    permission requirements. When you're acquiring a product, Black Duck Binary
                    Analysis allows informed decisions, minimizes your risk, and maximizes the value
                    of the product.

                Maintains security as threats evolve. The receipt of a detailed Bill of
                    Materials for every analyzed product keeps your supply chain secure. Black Duck
                    Binary Analysis automatically updates you when a new vulnerability applies to
                    previously scanned software. This information allows you to make decisions,
                    mitigate or eliminate risks, or negotiate with suppliers.

            

        

    

    Use Cases Addressed

        
        
            Black Duck Binary Analysis can be leveraged in a variety of situations, depending on
                who you are and what role you occupy in your organization:

            
                Procurement: If you are acquiring a product, Black Duck Binary Analysis
                    provides visibility into the risk profile of the product, allowing you to make
                    informed decisions and negotiate with your vendor to minimize your risk and
                    maximize the value of the product.

                Mergers and Acquisitions: Black Duck Binary Analysis makes it easy to
                    analyze existing products to understand their composition and associated risk.
                    Better visibility leads to better decisions about product integration and
                    security risks.

                Supply chain security: Any organization looking to minimize risk in its
                    supply chain can put Black Duck Binary Analysis's results to good use. For each
                    analyzed product, Black Duck Binary Analysis provides a BOM, an accurate view of
                    vulnerabilities and risk. This information allows you to make decisions,
                    mitigate or eliminate risks, or negotiate with suppliers.

                Development: For builder organizations, Black Duck Binary Analysis
                    provides automation for tracking third-party software components. As a critical
                    check on the products you are building, Black Duck Binary Analysis gives you the
                    information you need to verify that your product has exactly the components you
                    expect, that those components are up to date, and that no inappropriate software
                    licenses have been used.

            

        

    

    Why and How

        
        
            Using third-party code saves time and money, but exposes your project to risks, in
                terms of security, code quality, and licensing. Black Duck Binary Analysis addresses
                that risk when you don't have access to source code. It analyzes software binaries,
                compiled applications, or docker images. It can scan virtually any compiled
                software, including desktop and mobile applications, embedded system firmware, and
                more. (It does not analyze source code; however, standard Black Duck can do
                that.)

            Black Duck Binary Analysis recognizes thousands of existing libraries and open-source
                projects, as well as their components. If it does not recognize components because
                it is a proprietary or commercial component or it’s possibly a missing OSS component
                in the Knowledgebase, you can teach the components using the Vendor Components
                functionality in Black Duck Binary Analysis, and they will be recognized thereafter.
                (See the User Guide for more information.) You may also request adding an OSS
                component to the Knowledgebase by opening up a Support request.

            Black Duck Binary Analysis's composition analysis helps you determine whether any of
                your software components are vulnerable to bugs such as Heartbleed (CVE-2014-0160),
                particularly in cases where you either cannot run dynamic tests against your systems
                or are afraid that active vulnerability scanning might have adverse
                consequences.

        

    

    Basic Usage

        
        
            When you scan your code with Black Duck Binary Analysis, it analyzes your binary
                files and compares the results with those stored in a common database. Components
                can be recognized by a number of matching methods, including the use of metadata
                extracted from binary files or .jar files; package manager data, manifest files, or
                a checksum of a .jar file. (In the user interface, you can find the matching method
                that was applied to any file in its component description.)

            When you teach Black Duck Binary Analysis to recognize your components, you can track
                and manage the vulnerabilities that are found in them. These remain in your
                organization and are never shared in the common database (In fact, customers cannot
                add components or information to the common database – so your proprietary files
                cannot be mistakenly exposed).

            After scanning your application (including third-party and proprietary code), Black
                Duck Binary Analysis produces a bill of materials (BOM): a comprehensive listing of
                the components, their known vulnerabilities, and the associated software
                licenses.

            A comprehensive dashboard helps you manage vulnerabilities, leaks of potentially
                sensitive information, and licensing issues, discovered by Black Duck Binary
                Analysis. Additionally, you can download scanned binary files and add custom data to
                scan results.

        

    

    Obtaining and Setting Up Black Duck Binary Analysis

        
        
            Typically, licensed users can access and use Black Duck Binary Analysis in any of
                these ways:

            
                As a cloud application, in a SaaS environment that is hosted by Amazon Web
                    Services, via https://bdba.blackduck.com/. All files are encrypted with AWS KMS using 256-bit
                    AES-GCM encryption.

                As an on-premises software appliance (a virtual machine), accessed only through
                    your network and using your preferred hypervisor.

                Deployed on a Kubernetes cluster. For more instructions, see https://github.com/protecode-sc/helm-chart.

            

            Once installed, Black Duck Binary Analysis can be accessed through any modern web
                browser or by using a web API. When accessed by browser, the interactive dashboard
                displays a high-level overview of composition, overall health, and security risks of
                scanned software.

            Black Duck Binary Analysis supports single sign-on (SSO) via SAML. With SSO, users
                can log in via an Identity Provider and won't need separate login credentials for
                different services.


===== TOPIC: Requirements and Limitations =====
# URL: https://docs.blackduck.com/r/bdba-installation/2026.9.0/ (topic id ~xWVJu80IxCDaiBJEd7Vbw)

Virtual Machine Configuration

        
        
            
                We recommend the following resources:

                
                    Memory:
                            At least 12GB for the appliance.

                            At least 32GB (16GB for the appliance + 4GB per core (4 cores are
                                the minimum) if you are scanning large files (larger than 2GB) on a
                                regular basis.

                        

                    Network Speed: A minimum of 36Mbps is required to upload the maximum
                        file size (8GB) in under 30 minutes.That
                        is:

8096MB / 1800 (30min as seconds) = 4.5 megabytes per second.
Network speeds are usually measured in bits per second as opposed to bytes. Thus:
 4.5MB/s * 8 = _36Mbps_ (megabits per second)

                    Processors: A minimum of 4 CPUs.

                    Storage: 500GB.

                

                You might be able to get acceptable performance from fewer resources, depending
                    on your needs.

                If you import the virtual appliance from the
                        protecode-sc-appliance-<version>.ova file, then it will
                    be configured with the default values that are set in the OVF file.

            

        

    

    Distributed Mode Configurations

        
        
            
                We recommend the following resources for machines configured as workers in
                    distributed mode:

                
                    Memory: A minimum of 6GB is required, but 12GB is recommended.

                    Network Speed: A minimum of 36Mbps.

                    Processors: At least four cores.

                    Storage: 500GB.

                

            

        

    

    Limitations

        
        
            
                These limits apply:

                
                    File Size: No limit when uploading through the API. Limited to 8GB
                        per file when using the web UI (either to the cloud or the appliance).

                    Parallel Scans: One per core. A machine with four cores can scan four
                        files simultaneously. The appliance recognizes the number of CPUs available
                        when it boots, and it configures parallel scanning accordingly.

                    Session Timeout: A user session times out after 60 minutes when using
                        the cloud; sessions on a self-hosted appliance time out after two
                        weeks.

                    Upload Timeout: Uploading has its own timeouts. The limits are 30
                        minutes for the UI and 90 minutes when connecting through the API. These
                        limits are the same when using the cloud or the appliance.

                    Browsers: Black Duck Binary Analysis is tested with the following
                        browsers, using the latest version available at the time of release where
                        nothing else is mentioned.
                            Chrome

                            Edge (version 79.0.309 and later)

                            Firefox

                            Safari

                        

                

                Note: Support for Internet Explorer ended with the 2019.09
                    release of Black Duck Binary Analysis.

            

        

    

    Supported Hypervisors

        
        
            
                Black Duck officially supports the following hypervisors for Black Duck Binary
                    Analysis deployments:

                
                    VMware vSphere/ESXi (ESXi version 6.5 and
                        later)

                    KVM

                

                We do not recommend using VirtualBox for Black Duck Binary Analysis production
                    deployments. Although some customers have used VirtualBox for their deployments,
                    results have been mixed. We consider VirtualBox an acceptable option for
                    prototyping in local development environments, but recommend the options above
                    for deployment.

            

        

    

    Debian OS versions

        
        
            
                Black Duck Binary Analysis Virtual Appliance has been built on Debian OS 11.
                    Legacy Virtual Appliances have been built on Debian OS 9. From Black Duck Binary
                    Analysis 2021.12.0 onwards, versions of the Virtual Appliance on Debian OS 9 and
                    Debian OS 11 will be available. Support for the legacy Virtual Appliance on
                    Debian OS 9 will be dropped in September 2022.


===== TOPIC: Installing as a Virtual Appliance =====
# URL: https://docs.blackduck.com/r/bdba-installation/2026.9.0/ (topic id BjF5Sw_ZyuVIeqZICc7CZQ)

Importing to vSphere/ESXi

        
        
            
                From the Download Arena, you can obtain a Black Duck Binary Analysis virtual
                    appliance in OVA format. With a vSphere client, importing the OVA package is
                    straightforward. The OVA package includes default configuration values.

            

        

    

    Importing to KVM

        
        
            
                In KVM, you can import a virtual appliance in a number of formats. The
                        qcow2 format supports variable disk size, whereas the
                        raw format is fixed. These instructions assume that you
                    have already installed and configured KVM on your system.

                To import Black Duck Binary Analysis in qcow2 format, follow
                    these steps:

                
                    Unzip the protecode-sc-appliance-<version>.qcow2.xz file
                        that you downloaded from the Download Arena.

                    Enter the following
                            command: $ qemu-img convert -O qcow2 protecode-sc-appliance-<version>.qcow2.xz my-BDBA.qcow2The
                            last part of the command is the name of the output file, which you can
                            change. The output file is ready to be imported to KVM.

                

            

        

    

    Importing to VirtualBox

        
        
            
                With VirtualBox, you can deploy Black Duck Binary Analysis as a virtual appliance
                    locally. This can be useful if you want to familiarize yourself with the product
                    before production deployment. VirtualBox is not recommended for a production
                    deployment of Black Duck Binary Analysis.

            

        

    

    Deploying Black Duck Binary Analysis as a Virtual Appliance in VirtualBox

        
        
            
                
                    Select File > Import Appliance. Use the File System browser to
                        choose the protecode-sc-appliance-<version>.ova file
                        that you downloaded from Black Duck.

                    Select Continue.

                    In the Appliance Settings pane, make sure the Guest OS type is Debian
                        (64-bit). If it is not, select the Guest OS Type setting to reveal a
                        pull-down menu and select Linux > Debian (64-bit).

                    Select Import.Figure 1. The VirtualBox Manager
                            
                            
                        

                

                After importing the appliance, you should see your new virtual machine listed in
                    the VirtualBox Manager, however, it isn't ready to use yet.

                Note: 
                    You must configure port forwarding before using the machine.

                

            

        

    

    Configuring Port Forwarding

        
        
            
                
                    In VirtualBox Manager, select your Black Duck Binary Analysis virtual
                        machine from the list of machines on the left, then select Settings >
                            Network.

                    In the Network pane, toggle Advanced, and then select Port
                            Forwarding.Figure 2. Advanced options displayed in the Network pane
                            
                            
                        

                    Add the following two port forwarding rules. You can add a rule by selecting
                        the icon in the upper right-hand corner of the following window: Figure 3. Port forwarding rules as entered in VirtualBox
                            
                            
                        

When you enter port forwarding rules, the third and fifth columns
                            should remain empty.

                    Select OK to save the settings.

                    Select Start to boot the virtual machine.When VirtualBox finishes
                            loading your virtual machine, you should see the Black Duck Binary
                            Analysis console.

Figure 4. The Black Duck Binary Analysis Console
                            
                            
                        

You can now access Black Duck Binary Analysis through a web browser
                            by entering http://localhost:8000 in the address
                            bar.


===== TOPIC: Update Configuration =====
# URL: https://docs.blackduck.com/r/bdba-installation/2026.9.0/ (topic id 3qjKcWbJlu1FIt2eFtXcPQ)

Black Duck Binary Analysis should receive two types of maintenance regularly: system updates, and platform (OS) upgrades. These should be performed whenever updates are available.

A system update:

Includes the frontend (the UI), all workers, and the vulnerability database.

Does not require a direct Internet connection, but you will have to use the Internet to obtain the update files.

Can be configured to take place periodically and automatically.

A platform upgrade:

Includes updates to the underlying operating system of the virtual machine (It is similar to using sudo apt-get dist-upgrade).

Requires a continuous Internet connection.

Cannot be performed automatically.

Note: We've chosen to use "update" when talking about Black Duck Binary Analysis and "upgrade" when talking about the platform (the underlying operating system). This makes it easier to distinguish between the two operations, but there is no other significant difference between the terms.

Automatic System Updates

                To activate automatic updates, your appliance must have access to the Internet. Automatic updates require valid Download Arena or  credentials, which you should have received when you purchased Black Duck Binary Analysis.

                Contact Black Duck Support at https://community.blackduck.com/s/my-support-home if you have not received an account e-mail, if you have lost your password, or if you have any other questions concerning your account.

            

Configure Automatic Downloading of Updates

                To enable automatic downloading:

                From the Home page, Navigate to System settings.

Select Automatic update configuration.

Under the Change Arena or Community Credentials heading, enter your Arena or Community account username and password.

Select Save credentials.

                If you no longer wish to use automatic updates, clear the text fields and select Save credentials.

                Under the Platform update sources for Debian heading, you can change the default source URLs.

                Note: Debian officially does not support HTTPS for repositories; the package signing mechanism provides security instead. Official “ftp.country.debian.org” mirrors are aliases for multiple sites that do not have a certificate matching the alias. To use HTTPS, the real hostname of the mirror supporting HTTPS is required in the URL.

                Automatic updates include the following.

                 Your appliance syncs the component metadata with the remote vulnerability database and the remote component database once a day, as long as an internet connection is available and your Arena credentials remain valid. 

 Updates for the frontend and worker will be downloaded, when updates become available. 

 You will be notified that the updates are available, so that you can use them. 

                Although downloading is automatic, the installation must be started manually.

            

Component Signature Updates

Component signatures for matching components are updated with a new worker release but they can also be updated between releases, if necessary. In order to update component signatures between worker releases, an internet connection is required. Downloading and updating component signatures takes place automatically in the background.

Install an Update

To update the system, when an update is available:

Navigate to Home > System settings > Update system (The details about the new update can be found on this page.)

Select Start upgrade to implement the updates.

Approve Lists

If you limit access to your system by means of an approve list, include in your list the servers providing these updates for Black Duck Binary Analysis. They are:

Frontend & worker update: https://www.codenomicon.com and Black Duck Community.

Database update: protecode-sc.com

Automatic software updates (Appliance and Community in use):protecodesc.s3.us-east-1.amazonaws.com
            

Automatic signature updates:appcheck-keg-production.s3.eu-west-1.amazonaws.com

Vulnerability updates:https://bdba.blackduck.com
            

Platform security: http://security.debian.org/debian-security/

Platform: https://www.debian.org/mirror/list

Use the link above to find the nearest mirror repo for Debian. Add the repo (not the link above) to the list.

Manual Updates and Upgrades

You can manually apply both the system update and the platform upgrade.

If system updates are applied manually, two separate steps are required: one to update the vulnerability database and one for the rest of the system.Note: If you have previously enabled automatic updates, then you need to delete the credentials (username and password) of automatic updates to enable manual updates.

Vulnerability Database Update Frequency

NVD metadata is updated every 24 hours.

BDSA metadata is updated every hour.

Manually Updating the Vulnerability Database

If your appliance is not connected to the Internet, then you will need to manually update the vulnerability database at least weekly.

To manually update the vulnerability database:

Download the database update files in one of the following ways. (Choose only one.)For a regular weekly update Obtain the update by downloading bdba-onprem-data-update-YYYYMMDD-hhmmss.tar.zst from https://bdba.blackduck.com/updates-v2/.

If you haven't updated in more than a week Obtain updates from this address: https://bdba.blackduck.com/updates-v2/bootstrap

For a new appliance, or one you haven't updated in more than a month Obtain updates from this address: https://bdba.blackduck.com/updates/vulndata/.

When prompted, enter your Arena credentials or Community credentials (not your Black Duck Binary Analysis user credentials) and then download the file protecode-sc-updates.tar.zst.

In the Black Duck Binary Analysis user interface, navigate to System settings > Update vulnerability database.

In the "Perform a manual update" section, select Choose file OR Browse... (depending on your browser)

Select the file that you downloaded in step 1.

Select Upload and update.

Synchronizing the Vulnerability Database

If for some reason the Appliance has been offline for more than 30 days, there may be holes in vulnerability data. This is due to the fact that Appliance receives only updates for 30 days from upstream data source. To synchronize the database, go to "Settings -> Update vulnerability database" and click Full Synchronization.

During the Synchronization, scanning will be disabled for the time it takes to synchronize the database. This typically takes from 10 to 30 minutes.

In airgapped installations, you can download vulnerability data from https://www.protecode-sc.com/updates/vulndata and update it via manual vulnerability data update.

Applying a System Update

To manually update the system components, you will first have to obtain the system component files from https://www.codenomicon.com/arena or Black Duck Community.

In Arena, the Black Duck Binary Analysis system component files have the following naming conventions:

Frontend (code-appcheck-frontend-*.install)

Worker (code-appcheck-worker-*.install)

Both should be updated, if newer versions are available.

To apply the system update:

Navigate to System settings.

Select Update system.

Select the System tab (as opposed to platform).

Select Choose file OR Browse... (depending on your browser).

Select a file that you downloaded from https://www.codenomicon.com/arena.

Select Update and upload.

If you are updating both the frontend and the worker, then repeat steps 3 and 4 for each file.

When you apply updates, all your distributed workers are updated as well.

Applying a Platform Upgrade

Platform upgrades do not take place automatically, because they call for rebooting the system in certain cases. The platform upgrade process takes several minutes to complete and requires an active Internet connection throughout the process.

If you can connect your appliance to the Internet, then you can apply a platform upgrade.

To apply a platform upgrade:

Navigate to System settings.

Select Update system.

Select the Platform tab.

Select Start platform upgrade.
