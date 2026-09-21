# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q
# Reader base: https://docs.blackduck.com/bundle/blackduck-hub/page/
# Captured: 2026-09-21



===== TOPIC: Architecture and Network Communications =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id 05pTNfrPq_Qd55vosvFXuQ)




===== TOPIC: Black Duck architecture overview =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id toG7gnZ68omCh~cmf6kU7A)

Black Duck helps security and development teams identify and mitigate open-source related risks across application portfolios. Black Duck:

Scans and identifies open-source software throughout your code base

Maps vulnerabilities to your open-source software

Triages vulnerability results and tracks remediation

Monitors for newly disclosed vulnerabilities in your open-source code


===== TOPIC: Black Duck on-premise architecture overview =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id sb2_f7JfqyFbuAMXVK9fjA)

Black Duck's architecture consists of different components that work together to provide Black Duck functionality.

Black Duck Detect

Black Duck Detect consolidates the functionality of Black Duck and Black Duck Binary Analysis into a single solution. Black Duck Detect is designed to integrate natively into the build/CI environment and for Black Duck and Black Duck Binary Analysis, it makes it easier to set up and scan code bases using a variety of languages and package managers. Black Duck Detect performs the task of determining all the direct and transitive dependencies, collecting that data, and sending it to the customer's Black Duck server (as JSON data in BDIO format) for open-source software (OSS) matching. After determining the dependencies, it can also launch the Black Duck Scan Client to perform a variety of file scanning methods. Those methods and network communication requirements are described in the next section, The Scan Client. Black Duck Detect can also run a Black Duck Binary Analysis (BDBA) scan in conjunction with other scan methods. This method and its network communication requirements are covered in Chapter 2.

A few key points about Black Duck Detect:

Black Duck Detect typically runs in a network-enabled environment and typically downloaded via a curl command from https://detect.blackduck.com. However, this is not required and Black Duck Detect can run in an air gap environment. If running Black Duck Detect in an air gap environment is desired, click this link in the Black Duck Detect documentation about how to configure this mode of operation.

Black Duck Detect can be run offline and the contents examined. The content is JSON data in BDIO format.

For information on the BDIO spec, click this link.

For additional information on how to run Black Duck Detect in an offline mode, click this link.

Black Duck Detect can run independently of a scan on the customer's Black Duck server, or it can be configured to wait for the Black Duck scans to complete so it can retrieve additional information. Typically, this is done if a user wants to fail a build due to a policy violation or collect a post scan report and store it as a build artifact.

Black Duck Detect does use Google Analytics to collect anonymized usage metrics which helps to set engineering priorities. In a network where access to outside servers is limited, this mechanism may fail, and those failures may be visible in the log. This is a harmless failure; Black Duck Detect will continue to function normally. If you wish to disable this mechanism, click this link for instructions.

The Scan Client

The Scan Client performs the task of scanning a file system, collecting data, and sending it to the customer's Black Duck server for open-source software (OSS) matching. This software always runs locally, on the customer's premises or wherever the files to be scanned are located. As the Scan Client examines the files, it generates “signatures” of the files and directories it is scanning and collects other metadata like file path and file/directory sizes in order to accurately identify open-source code; refer to the diagram on page 1 to see what is additionally sent. This information is used to match against information in the Black Duck KnowledgeBase to determine the open-source components/versions that are contained in the software being analyzed. As part of its operation, if the Scan Client can connect to the specified customer's Black Duck server, it will check its current version against that server and update itself if necessary.

There are various options for running the Scan Client – it can be used via Black Duck Detect and integrated into CI Tools (for example, Jenkins), standalone (either with a CLI or GUI), or as a Docker container for scanning other containers. The typical best practice is to run the scan client as part of Black Duck Detect.

In addition to running a component-level signature scan, the client can also optionally perform other scan functions. If desired by the end user, it can also:

Run a type of string search analysis on textual-based files looking for license text and copyright statements.The string search matches only return the match category, file name, and byte offset (location inside the file) where the match was found.

For copyright matches, it also uploads textual content (the copyright statement).

Wait for component analysis to complete and scan unmatched files for OSS snippets.Snippet scanning creates codeprints (one-way cryptographic hashes) over fragments of the files via a sliding window method which are then used to match for OSS.

It does not capture, store, or send any textual file content to the Black Duck KB for analysis. All code stays behind the company firewall. Only hashes are transferred.

Encrypt and upload scanned source to the customer's Black Duck server for snippet side-by-side comparison, or license and copyright display in the Black Duck UI.Uploading code is an optional feature that must be enabled at the server and scan levels.

If the server is enabled for source upload (which includes defining a company-specific encryption key) and the user indicates they wish to upload source files, the client will encrypt and upload the OSS files scanned for snippets and strings to the customer's Black Duck Server. See the Black Duck upload service section for more information.

Most of these activities can be controlled either at the customer's Black Duck Server level if the behavior is not desired. For example, if required by company policy, one can set the customer's Black Duck server to:

Not accept upload of encrypted source files.

Not send file/path name information.

Not sending up the source files can impact a user’s ability to triage matches, however it does not affect the quality of the Bill of Material, or “BOM”. It is up to individual customers policies to enable this feature and by default it is off.

However, not sending the file and path names to the customer's Black Duck server can lead to inexact component matching and a poorer quality BOM. Therefore, this feature is on by default and Black Duck recommends that customers do not disable it as using this information leads to stronger, more accurate matching. If file/path information is not desired to be uploaded, this can be controlled with the KBMATCH_SENDPATH system parameter. Instructions on how a system administrator can configure system parameters is included in the appropriate installation guides for your container orchestration platform.

Note: The KBMATCH_SENDPATH parameter has been deprecated as of 2023.4.0 and will be removed in a future update. Black Duck users with Match as a Service (MaaS) enabled will not be able to use this parameter. Customers wanting to continue using this option will need to contact Black Duck support to have MaaS disabled for their Black Duck registration keys.

Black Duck web application

Once the scan is completed, the Scan Client sends the signatures to Black Duck's web application. Black Duck's web application, accessed via a browser, provides a central point for managing and viewing all the information captured. User connections to Black Duck's web application (from a browser or other supported client) are secured using HTTP/2 and TLS1.3 (or HTTP 1.1 and/or TLS 1.2 if the browser does not support HTTPS/2 and/or TLS 1.3).

The Black Duck application will send the signatures to the Black Duck KnowledgeBase (KB) web service to identify the open-source software contained in the code which has been scanned and retrieve the associated metadata for each component. It will then generate a BOM, which details the open-source components/versions and presents the associated risk factors – security risk, license risk, and operational risk.

End users can review and edit the BOMs, filter results based on risk and other factors, and drill down to get more detailed information on the vulnerabilities, licenses, files, and other information associated with each of the components in the BOM. The Black Duck application also includes features such as policy management, search, vulnerability mitigation status and tracking, reporting, and so on.

The Black Duck application is built on top of various open-source components – such as Apache Tomcat web server, PostgreSQL database, and so on. The Black Duck application is deployed and managed as a set of Docker containers and supports a range of container orchestration platforms. More information on these containers is included in the Black Duck installation guide.

A few notes about the Black Duck web application:

The web application can make frequent calls to both the Black Duck KB and Black Duck registration services. To get full operability of the system, those services must be accessible by the server. The endpoint for the KB is kb.blackducksoftware.com and the registration service endpoint is updates.suite.blackducksoftware.com. For more information on making those services accessible, click this link to view the relevant community article.

For additional information about communication between the Black Duck web application and the various services, see the Communication with Black Duck services section.

Black Duck upload service

Customers can optionally decide to upload their source files to be used in reviewing snippet matches or embedded licenses and copyrights in the Black Duck UI. If not enabled, the system will still function, however users will not be able to view match content in the UI.

If enabled, the customer system administrator uses a Docker secret to provide a key that encrypts a Black Duck generated master key, which is used for encrypting and decrypting the customer's source files. The master key is stored encrypted (AES-GCM-256 with a key length of 32 bytes) via the customer-provided key. Information on how to set this up is included in the Black Duck installation guide for your particular container orchestration platform.

During a scan, the scan client sends the source file contents to the Black Duck instance via SSL/TLS-secured endpoint(s) and with the proper authorization token. An upload endpoint receives the source file contents via HTTPS. Access to the endpoint is secured via the generated and verified Black Duck JSON Web Token (JWT). The source files are stored via their associated file signature – no files are stored with their file name. Files are encrypted upon upload via the master key.

The web application requests the file contents via the given file signature. The source file is transmitted via HTTPS over the network. The individual source file is unencrypted for viewing in the Black Duck web application via the master encryption key.

In addition to encryption, the uploaded files also are deleted according to the data retention policy as defined by the customer. See the Data retention policy section for more information.

Web services hosted on customer's Black Duck servers

The Black Duck application works in conjunction with services that are hosted in Black Duck data centers. These services are:

Registration service: Used to validate Black Duck software license and entitlements.

This service is datacenter-managed by Black Duck in Massachusetts, USA.

Black Duck KnowledgeBase (KB): Contains meta-data (versions, signatures, licenses, vulnerability data, and so on) on all the open-source projects tracked by Black Duck. As a web service, the KB provides real-time updates, for example, new components or versions, vulnerabilities, and so on, which are immediately available to the Black Duck application.

The KB resides on Google Cloud Platform (GCP) Services with a variety of locations. Currently the KB is running of an instance of GCP in North America, Europe, and Asia.

It is possible to force the location of the KB onto one GCP geographical location. Failback mechanisms, in case one instance is down, can also be disabled.


===== TOPIC: Communication with Black Duck services =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id HduYuIV76HlaU91skcwFJw)

Black Duck interacts purely as a client of the servers hosted by Black Duck at secure data centers. Black Duck understands that Black Duck is being used in conjunction with our customer's valuable software intellectual property and treats the Internet-based communications between a customer installation of our products and the data center servers with due care, ensuring that no scanned code or proprietary customer data ever leaves the customer's premises.

All information sent to the customer's Black Duck SCA servers is treated as confidential information by Black Duck in accordance with our customer agreements. By default, all communication with Black Duck servers is done via HTTPS. More specifically, all data being transmitted is encrypted with TLS 1.3 (or TLS 1.2 if the client does not support TLS1.3). Customer sites always initiate connections with Black Duck SCA services; the hosted Black Duck SCA services never call out to the Black Duck application. The customer's Black Duck servers contain the HTTPS certificate, the Black Duck application initiates all connection requests using the certificate’s public key.

The information that is sent to the KB web services is for retrieving other information needed by the Black Duck application, for example, open-source metadata. Black Duck SCA does not retain any sensitive customer application data on its servers. Customer data is used by the KB matching service and retained on the server only during this ephemeral matching process. Once completed all customer data, including filenames, is deleted. No data is retained whatsoever.

More details on the specific communications between a customer site installation of Black Duck and the Black Duck services are included below:

Registration service

KnowledgeBase service

Black Duck Hosted customer instances monitors

SCA scan service


===== TOPIC: Considerations for SCASS =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id obLwtJtD~iHCUuctj26IYA)

As organizations increasingly rely on the SCA Scan Service (SCASS) hosted at scass.blackduck.com, it is essential to address the security aspects of the communication sessions involved. This section provides an overview of security considerations, clarifications on data handling, and guidance for customers to ensure a smooth rollout of SCASS.

Security Concerns
In our engagement with customers, concerns were raised regarding the security of communication sessions with the SCASS service. Key points of concern include:

The nature of data transmitted between systems.

The internal processing changes and their implications for security.

Assurance that the SCASS rollout complies with the customer’s security protocols.

Clarification on Data Transmission
In response to these concerns, we want to clarify the following:

No Changes to Data Transmission:

There have been no alterations to the data that is transmitted between our systems. The integrity and confidentiality of the data remain intact.

Internal Processing Changes:

The modifications made are solely related to how we internally process queries and data. These changes are backend improvements and do not impact the customer experience or data handling practices.

Exception for Binary and Container Scanning:

It is important to note that the only exception to this is with binary and container scanning features, which have not yet been rolled out. Customers should be aware of this when planning their usage of SCASS.

Implementation Guidance
To facilitate a successful implementation of SCASS while addressing security concerns, we recommend the following steps for customers:

Review Security Policies:

Ensure that your organization's security policies align with the use of SCASS and that all team members are aware of the changes.

Engage Security Teams:

Involve your security officers in reviewing the clarifications provided to ensure that all potential risks are assessed and addressed.

Monitor Rollout Progress:

Keep track of the SCASS rollout and any updates regarding binary and container scanning features. Stay informed about any changes that may affect security practices.

Provide Feedback:

Share any further concerns or feedback with your Black Duck representative to ensure that your security needs are met effectively.

The security of communication sessions with SCASS is of utmost importance. By understanding the nature of the changes and taking proactive measures, customers can confidently roll out SCASS while maintaining robust security practices. For additional questions or support, please contact your Black Duck representative.


===== TOPIC: Data retention policy =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id k3xgUzADuSM9d4VMXZNgyw)

Black Duck stores all sensitive customer data locally, behind the customer’s firewall, including projects, components, and vulnerabilities. No binary files or proprietary customer data (projects, BOMs, licenses, vulnerabilities, and so on) is ever sent to Black Duck or the KnowledgeBase. No source code is sent to Black Duck unless the customer has enabled the uploading of source files. If a customer has enabled uploading source files, the encrypted source files are retained for 180 days and then deleted; customers can configure a different data retention period with the DATA_RETENTION_IN_DAYS system parameter as described in the Black Duck installation guides.

Registration keys are used to authenticate web requests. Once a request is successfully authenticated, no customer-specific information is retained:

IP addresses from the originating requestor are “stripped” by the load balancer.

All weblogs retained for operational purposes do not contain session data.

All data that is retained for KB improvement (statistics related to web service requests) is anonymized – there are no identifiers which can be used to associate a customer to a particular KB request.


===== TOPIC: Configuring AI-Assisted Documentation Service =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id w0xQd0TKa3y8WTFsiML9fA)

The AI-Assisted Documentation Service provides in-application access to Black Duck SCA documentation through an AI-powered search experience. Users can search documentation content and view relevant results without leaving the application.

When the AI-Assisted Documentation Service is disabled, Black Duck SCA uses the legacy documentation experience instead. Air-gapped deployments always use the legacy documentation experience.

Note: AI-Assisted Documentation Service is enabled by default.

Requirements
To configure the AI-Assisted Documentation Service, you must have the System Administrator role.

Enable or Disable the AI-Assisted Documentation Service
Log into Black Duck SCA with the System Administrator role.

Click Admin → System Settings.

Under System, click Help.

Enable or disable the AI Assisted Documentation Service setting.

Service Behavior
The behavior of the documentation experience depends on the selected setting.

Setting
Behaviour

Enabled
Users can access AI-assisted documentation search from the Help menu.

Disabled
Users are directed to the legacy documentation experience.

Air-gapped deployment
The legacy documentation experience is always used.

Data Collection and Privacy
When the AI-Assisted Documentation Service is enabled, documentation search requests are processed by an external cloud-based service to provide AI-assisted search functionality.

Organizations that do not want documentation search requests processed externally can disable the AI-Assisted Documentation Service. When disabled, Black Duck SCA uses the legacy documentation experience instead.

The AI-Assisted Documentation Service does not place cookies in the user's browser.

Note: Air-gapped deployments cannot use the AI-Assisted Documentation Service and continue to use the legacy documentation experience.

Access AI-Assisted Documentation
When the AI-Assisted Documentation Service is enabled:

Click the Help menu in the top navigation bar.

Select Documentation Search.

The documentation search panel opens, allowing you to search Black Duck SCA documentation directly from within the application.


===== TOPIC: About Black Duck - Binary Analysis =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id T_pWWoB7PhWX8BuEWn7Kuw)

Black Duck Binary Analysis(BDBA) identifies the open source security, compliance, and quality risks in the software libraries, executables, and vendor-supplied binaries in use within your codebase. BDBA supports expanded file type support including various firmware formats, filesystems/disk images, installation formats, and various compression and archive formats. With Black Duck Binary Analysis, you can:

Analyze virtually any compiled software, firmware, mobile applications, or multiple installer formats, without needing to access the source.

Identify embedded open source usage and risks within binary executables and libraries.

Manage code decay and improve software quality within binary dependencies.

Monitor new vulnerabilities in previously scanned binaries.

After installing Black Duck - Binary Analysis:

Use Black Duck Detect to scan your software or firmware.

View the results of your scan in a comprehensive project version BOM.

For you to easily identify these files, the BOM displays the match type as Binary.

Use the BOM to identify known vulnerabilities and licensing obligations within software components.

Refer to the installation guides for more information on installing Black Duck with Black Duck - Binary Analysis.


===== TOPIC: Increasing the size of the binary scan file =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id Hik~ToHvxwFTOsldxtmAwg)

When using Black Duck Binary Analysis, the maximum size of the binary that can be scanned is 100 GB. You can increase this limit by adding the environment variable BINARY_UPLOAD_MAX_SIZE to the docker-compose.local-overrides.yml file or by setting this globally in blackduck-config.env and specifying a value in megabytes.

For example, to increase the maximum binary scan to 10 GB, add the following:

webserver:
    environment:
        BINARY_UPLOAD_MAX_SIZE: 10240m
storage:
    environment:
        BINARY_UPLOAD_MAX_SIZE: 10240m
scan:
    environment:
        BINARY_UPLOAD_MAX_SIZE: 10240mAfter updating the file when deploying the stack, ensure that the docker-compose.local-overrides.yml file is included as a command line parameter in the deploy command:

docker stack deploy -c docker-compose.yaml -c ... -c docker-compose.local-overrides.yml
