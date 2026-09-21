# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q
# Reader base: https://docs.blackduck.com/bundle/blackduck-hub/page/
# Captured: 2026-09-21



===== TOPIC: Manually adding an AI model to a BOM =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id zoj9KPWc20P8Nn~0AfuSYg)

Black Duck supports the ability to add AI models to your Bill of Materials (BOM), allowing for comprehensive tracking and management of AI components within your projects. This feature enables organizations to maintain visibility into the AI models they use, monitor associated risks, and ensure compliance with relevant policies.

This section will walk you through the process of adding AI models to your BOM, configuring their properties, and managing them effectively within your project ecosystem.

Prerequisites
Before adding AI models to your BOM, ensure the following requirements are met:

Feature Activation

The AI Model Scanning feature must be enabled on your product registration key. If you do not see this functionality in your Black Duck instance, please contact your Black Duck representative or support team to have this feature activated for your organization.

User Permissions

To add and manage AI models in a BOM, you must have appropriate permissions, including:

Project access with editing capabilities

BOM Management permissions

Scan Configuration

You must have performed a Detect scan using the following parameter:

--detect.blackduck.signature.scanner.individual.file.matching=ALL

Adding an AI model to a BOM
Adding AI models to your Bill of Materials follows a similar workflow to manually adding components. This streamlined process ensures consistency in your BOM management practices.

Navigate to the Project Version

Access your project list from the main dashboard.

Select the specific project and version where you want to add the AI model.

Access the BOM

Click on the Components tab to view the current Bill of Materials.

Initiate the Add Process

Locate and click the Add button near the top of the BOM view.

From the dropdown menu, select AI Model.

Enter AI Model Details

In the dialog that appears, provide the following information:

AI Model: Enter the name of the AI model.

Commit: Specify the commit version of the AI model.

Optionally, provide additional details by expanding the Advanced Attributes section:

Enter the Purpose for adding this component.

Select Modification if you modified this component and optionally, enter information regarding the modification.

Confirm and Save

Review the entered information

Click "Add" or "Save" to add the AI model to your BOM


===== TOPIC: About Container Scanning =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id qnnzjOi0E64I4rEnrgTt6g)

Container scanning improves the user experience for managing risk found in containers enabling you to manage the risk by container layer. When scanning a container using this feature, Black Duck SCA creates a new type of project that manages a new container scan. The container project displays the aggregated BOM and risk, but it also provides a way to view risk layer by layer, specifically adding support for components that are added or removed on a layer.

Note: In order to take advantage of this feature, you must have Black Duck Secure Container (BDSC) enabled on your product registration key.

Supported Container Image Formats
The following container image formats are supported under the Secure Container module:

Docker

Docker is one of the most widely used container image formats, allowing developers to package applications and their dependencies into standardized units. Black Duck SCA provides comprehensive scanning for Docker images, enabling users to identify vulnerabilities and manage risks effectively.

OCI (Open Container Initiative)

OCI is a set of open standards for container images and runtimes that promotes interoperability and compatibility across different container ecosystems. Black Duck SCA supports OCI images, ensuring that users can scan and analyze these containers for vulnerabilities and compliance with security policies.

Chainguard

Black Duck SCA Secure Container supports Chainguard container images, providing organizations with enhanced security for commercially maintained containers. This integration combines Chainguard’s curated component inventory and vulnerability intelligence with Black Duck SCA’s analysis capabilities, resulting in more accurate vulnerability detection, quicker access to security fixes, and reduced manual triage efforts for developers and security teams.

How do I perform a container scan?
Container scans are performed with Detect by using the following option during a scan:

--detect.tools=CONTAINER_SCANSee Container Scanning in the Detect documentation for more information on the container scanning process.

What is a container layer?
When Docker builds an image, the image is composed of layers which represent a specific modification to the container. These modifications can include commands such as RUN, COPY, FROM, etc.

What is a container project?
The output of a container scan automatically creates a container project in Black Duck and associates the scan to the project as a project version. This project version cannot have any other type of scan type. Multiple container scans can be mapped to a single project version.

The following are valid combinations of scans (code locations) that can be mapped to single project version:

Any combination of non-container scans mapped to project version.

One or many container scans mapped to project version.

One or many container scans along with one or many IaC/Malware scans mapped to the same project version.

All other combinations of mapped code locations are invalid and the scan process will fail if the mapping of corresponding code location will result in invalid combination.

When you open the resulting BOM, the project's header will indicate that it is a container project:

To view the containers mapped to this project version, click the  button. This will open a search model from which you can either type the name of the container you want to view or you can select it from the presented list.

What is in a container project BOM?
The BOM created during a container scan is, in many ways, the same as a regular BOM generated by other scanning processes with a few differences:

The left side of the container scan BOM displays a list of components found by layer.

Here you can find more details on security risks found throughout the container. By defaut, only the layers with security risks will be displayed but you can check the Show Empty checkbox for a complete list of all layers in the container.

Layers containing security risks display the following information:

The layer where the security risks are found.

The count of components with critical, high, medium, low, or no security risks.

The file size of the layer.

The number of components added or removed from the container.

Clicking the individual layers updates the table in the right-hand pane which displays specific details on the components and security risks found on that layer. On layers where components have been removed, the removed components will be grayed out indicating that no action is required to remedy this security risk.

The container scan BOM does not have a Source tab which would allow you to manage the files associated with BOM components.

What can I do with a container scan BOM?
As mentioned above, a container scan BOM is much like a regular BOM. For more information on how to manage the information in a BOM, please see Understanding the information in a project version's BOM.


===== TOPIC: Viewing component versions with encryption =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id ObGyQJ7WOTwYr3RSti2xRw)

Attention: This feature is not enabled by default in Black Duck and must be activated by adding the feature to your Product Registration key.

Open source software can use or implement cryptographic algorithms which can impact your organization from security and compliance perspective.

On the compliance side, whenever you send software out of the country – for example, on a computer, as source code, or compiled into an application that is for sale – depending upon where you live, you may be required to adhere to certain governmental regulations regarding the export of cryptography. This is especially true of strong cryptographic algorithms which may require licenses to export, however the regulations have eased in recent years.

On the security side, companies may be interested in understanding if open source is using weak cryptography or obsolete hashing mechanisms. Using a cracked (or insecure) cryptographic algorithm can add unnecessary risk to your organization, especially if well-known techniques exist to break the algorithm. Understanding algorithms in use can help companies comply with security standards.

Black Duck helps you identify the component versions that have encryption algorithms.

A cryptography filter in the component version BOM page identifies those component versions with encryption.

A cryptography icon () appears in the BOM page for any component version with encryption algorithms.

Select the component version to open the Component Version page and then select the Cryptography tab:

The table lists the encryption algorithms found in this component version.

The warning symbol () indicates that this algorithm has a known weakness.

Select an algorithm from the table to view more information, such as a description, key lengths, originator, licensing, and patent information.

Possible values for key lengths, with key length values where applicable, are:

Single Fixed Key Length

Multiple Fixed Key Lengths

User Definable Key Length within a Closed Range

User Definable Key Length Unconstrained

No Encryption or No Key Used

Note that the Cryptography tab does not appear if a component version does not have encryption algorithms.

Note: While components added manually to existing BOMs will display cryptography information, legacy BOMs may require a rescan for cryptography data to appear.

For more information on federal regulations, visit the Bureau of Industry and Security's (BIS) website: https://www.bis.doc.gov
