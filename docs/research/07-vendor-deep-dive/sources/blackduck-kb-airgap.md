# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/YsDtm_HKwGM6efkx~2HVvQ
# Reader base: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/
# Captured: 2026-09-21



===== TOPIC: Installing the Black Duck Air-gapped KnowledgeBase =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id _Nzcpqaq0Yl2BE9AXPOghA)

This guide describes the process of installing the Black Duck Air-gapped KnowledgeBase.

		Installation process

			
			The process to install and configure a Air-gapped KB with Black Duck SCA
				consists of the following steps:

			
				
					Downloading the software, data, and orchestration files from Google Cloud

				

				
					Setting up the Air-gapped KB server

				

				
					Installing Black Duck SCA

				

			
			The directions in this guide are based on the assumption that the artifacts are
				captured on a removable storage device and deployed on an air-gapped system.

		

		Requirements

			
			The following requirements assume you're downloading the artifacts using an Ubuntu
				machine.

			
						
							Devices, Software, and Files
							Requirements
						

					
						
						
							Computer with internet access
							
								
									Latest version of cURL
								

								Use the sudo apt install curl command to install
									on Ubuntu.

								
									Google command-line tools 
								

								Use curl https://sdk.cloud.google.com | bash to
									install on Ubuntu.

							
						

						
							Air-gapped system
							
								Operating system: Ubuntu 20.04 LTS or newer

								CPU: 64 cores

								RAM: 256 GB

								Disk capacity: minimum 35 TB SSD storage

								Make available to /var/lib/docker, which should be an expandable
									mount to account for future data growth.

							
						

						
							Removable media
							
								
									Minimum 8 TB
								

								Media used to get the data from GCP buckets to the air-gapped
									network.

							
						

						
							Software
							Latest version of Gzip: uncompress Air-gapped KB artifacts.
									Use sudo apt install gzip to install on
									Ubuntu.
Docker Compose: Latest 1.x
										version
Docker Community Edition: Latest
									version
To install on Ubuntu, follow instructions on https://docs.docker.com/engine/install/ubuntu/

						

						
							Files provided by Black Duck Support
							
								Key file to activate Google Cloud account, for example,
									kb-onprem.json.

								Black Duck license file: suite_v1.xml

							
						

					
			Important: Black Duck recommends that you to start the download to your device
				overnight to optimize your time. The Air-gapped KB artifacts to be downloaded are
				approximately 5 TB in total size.


===== TOPIC: Regarding big data infrastructure =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id wR0D_kOnrPkLMkLGJXu5Hg)

Black Duck Air-gapped KnowledgeBase does not offer support for big data infrastructure for Black Duck SCA
            that powers features like File Level License Data, Copyright Data, Actual License
            text.

        
            
                Black Duck SCA users who generate a Notice Report for a BOM will not see copyrights for
                    components and will only see template license texts for identified components with
                    licenses.

            

            
                Black Duck SCA users who use the application to explore Deep License Data on project BOMs
                    will not see any information on the file level for a selected component.

            

            
                Black Duck SCA users who use the application to explore Copyright information through the BOM
                    will not see any information on the copyright tab page.


===== TOPIC: Downloading software and data files =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id IYF3WWF_CMpcRQsl_anFww)

This chapter describes how to download the software and data files needed to install a
				Black Duck Air-gapped KnowledgeBase.

		These files are located on the Google Cloud. To download the files, you must do the
			following tasks:

		
			
				Install Google command line tools.

			

			
				Activate your service account and download the files.

				Note: All the commands in this guide can be executed by the root user, or a user
						with sudo privileges.

			

		
		Prerequisites

			
			You need the following prerequisites to complete the tasks described on this
				page:

			
				
					Computer with access to the internet

				

				
					Portable storage with a minimum of 8 TB of storage, which is attached to the
						computer with internet access.

				

				
					Google command-line tools, which you can install using the following command
						on an Ubuntu system:

					curl https://sdk.cloud.google.com | bash
				

				
					The key file: kb-onprem.json that you receive from Black Duck
						Support. This file is required to activate your Google service account.

				

			
			Note: Black Duck recommends that you consider an overnight schedule for this task as
					extracting the data will be a time-consuming process. Also, be aware of internet
					bandwidth requirements for this large download and consider downloading the
					artifacts overnight as the download size for the artifacts is about 5 TB.

		

		Activating your service account

			
			Activate your service account from the system you will use to download the software
				and data.

			
				
					Activate your Google service account.

					Locate the kb-onprem.json file on your system and run
						the following command:

					
						
							gcloud auth activate-service-account --key-file=kb-onprem.json

						

					
					Expect to see the following message when you authenticate successfully:

					Activated service account credentials for:
[kb-onprem-ro@kb-onprem.iam.gserviceaccount.com]
					Note: If you have any issues authenticating, contact Black Duck support and
							include any error messages.

				

				
					Access and download the artifacts.

					The Google Cloud bucket is divided into two high level folders: software and data. Black Duck stores three software releases in the
						bucket, which consists of the Current_GA (latest) and two previous
						releases.

					To simplify the separation of KnowledgeBase artifacts from Black Duck
						artifacts, the software is shipped as the following three components:

					
						
							KB Services: contains all artifacts necessary to build a KB Server.

						

						
							Black Duck: contains all artifacts to build Black Duck Hub instance.

						

						
							Orchestration: orchestration to bring up both, KB and Black Duck SCA instances.

						

					
					Tip: 
						Black Duck recommends executing the download steps
						overnight to avoid waiting for the download to finish as the data artifacts
						are about 5 TB in total size. 
							
								If you are using portable storage, ensure that the portable
									storage is connected before downloading to that storage. 

							

							
								Black Duck recommends using tmux for this
									session because it's a time-consuming step.

							

						

					To download the latest version of the software, use the following commands:

					
						
							gsutil cp -r gs://kb-onprem-us/2025.11/Orchestration
									<destination_path>

						

						
							gsutil cp -r gs://kb-onprem-us/2025.11/KBServices
								<destination_path>

						

						
							gsutil cp -r gs://kb-onprem-us/2025.11/BlackDuck
								<destination_path>

						

					
					Note: Replace 2025.11 with the current YYYY.MM. Run gsutil ls
							gs://kb-onprem-us/2025.11/Data/01 to see the data that exists
						in the 2025.11 release.

					To download the other data sets, use the following commands:

					
						
							gsutil cp gs://kb-onprem-us/2025.11/Data/01/*tar.gz <destination>

						

						
							gsutil cp -r gs://kb-onprem-us/2025.11/Data/01/ikb_match/
									<destination>

						

						
							gsutil cp gs://kb-onprem-us/2025.11/Data/fingerprints_*.gz
									<destination>

						

					
					Tip: Using gsutil -m cp enables multi-threaded downloads and can
						significantly improve performance if you are performing operations on a
						large number of files over a reasonably fast network connection. However, it
						can consume a significant amount of network bandwidth and cause problems or
						make your performance worse if you use a slower network.

					To list folders, use the following command:

					
						
							ls gs://kb-onprem-us/

						

					
					Tip: At the end of every month, an
						announcement is made on the Community website, which includes links to that
						month’s software and data release. Your Black Duck
						representative can also provide this information

				

				
					Configure the Air-gapped KB
						server.


===== TOPIC: Setting up the KnowledgeBase Server =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id X~ycdfVe3LryvEd2~Amohw)

This chapter lists the requirements and describes the process of setting up the Black Duck Air-gapped KnowledgeBase server.

		Prerequisites

			
			The following are the system requirements to install and configure the Air-gapped KB.

			
				
					Operating System: Ubuntu 20.04 LTS or later

				

				
					Docker Community Edition: Latest version

				

				
					Docker Compose: Latest 1.x version

				

				
					CPU: 64 cores

				

				
					Memory: 256 GB RAM

				

				
					Available Disk Space: Minimum of 35 TB available to
							/var/lib/docker, which is the default docker
						location.

					This mount should be expandable (not on the root partition), as should the
						source of the storage to enable data growth.

				

			
			Note: Black Duck recommends using solid state drives because of
				their better performance and I/O speeds.

		

		Installing and configuring the Air-gapped KB

			
			To install and configure the Air-gapped KB:

			
				
					Copy software and data files to the air-gapped machine.

					Note: The assumption is that you are copying the software and data that is
						downloaded from the Google Cloud bucket from portable storage on to the
						air-gapped system. This step might take a long time because the data is
						about 2 TB.

					Tip: Use a tmux session to execute commands for each step. Refer to
							https://linuxize.com/post/getting-started-with-tmux/ for more
						information. The FAQ section has an example on how to get a tmux session
						running.

					
						
							To copy software from portable media:

							Create a folder for data and a folder for software on the target
								machine and then copy the software as shown in the following
								example.

							For example on an Ubuntu system, to copy the software from the
								portable media to the air-gapped machine, on the air-gapped machine
								use the following commands:

							mkdir ~/software
cp -r <source_path> ~/software
							The source path is on the portable storage media.

						

						To copy data from portable media:

							Copy the data from the portable media to the storage mount point at
								/var/lib/docker/ into a data folder by using the following
								command:

							cd /var/lib/docker/
mkdir data
cp -r <source_path> /var/lib/docker/data
							When all the data is copied over, create a single extract folder and
								extract the tarballs into that folder.

							Tip: If using tmux, it would be good to extract the tarballs
								in parallel in different tmux window sessions to save time.

							Note: If you don't want to use snippets, you can skip the fourth and
								fifth tmux sessions

							cd /var/lib/docker/data/
mkdir extract
							First tmux session named solr

							tar -xvzf kb_search_*.tar.gz -C extract/
							Second tmux session named kb_spider

							tar -xvzf kb_spider_api_*.tar.gz -C extract/
							Third tmux session named kb_snippet

							tar -xvzf snippet_db_*.tar.gz -C extract/
							Fourth tmux session named ikb_match

							cd ikb_match
chmod +x extract.sh
./extract.sh --target=/var/lib/docker/data/extract/
							Fifth session named fingerprints

							tar -xvzf fingerprints_*.tar.gz -C /var/lib/docker/data/
							This process might last for several hours, depending on the I/O
								device. After the data is extracted, you can set up the Docker
								images.

						

					
				

				
					Set up the KB images. For this step, the Docker daemon must be up and
						running. Ensure Docker is installed correctly; to verify, use the
							sudo docker ps command.

					
						
							Navigate to the KBServices folder and load the
								Docker images by using the following commands.

							cd ~/software/KBServices/
sh load_images.sh
							It's helpful to check if there are any existing images and containers
								loaded by using the following commands:

							docker images ls
docker container ls
						

					
				

				
					Create and mount data volumes.

					
						
							To create Docker volumes for the data to be mounted: 

							Navigate to the setup folder in the kb-orch/setup/
								structure, and use the following commands:

							cd ~/software/Orchestration/
tar xf kb-onprem*.tar
cd kb-orch/setup
sh create-volumes.sh
							To verify volume creation, use the following command:

							docker volume ls
							When the volumes are created, stay in the same setup folder and use
								the following steps to mount the data into the created volumes.

						

						
							To mount the data, you must recall the path where you extracted your
								data archives. In the example, we used
									/var/lib/docker/data/extract.

							Note: This is a time-consuming step. To continue working in parallel,
								use tmux for the following set of commands.

							The setup files are configured to move extracted data into the mount
								location, and then give the docker containers access to it as the
								configured users. Since data is being moved instead of being copied,
								space is saved.

							Tip: If you have a data extracted on the same mount location
								where your volume is (same logical partition) the move should be
								instantaneous. However, if you are using slower storage, or copying
								from outside the logical partition, execute this in a tmux
								session.

							To mount data sets, use the following:

							sh setup-api-data.sh /var/lib/docker/data/extract/
sh setup-search-data.sh /var/lib/docker/data/extract/
sh setup-match-non_baseline.sh /var/lib/docker/data/extract/
sh setup-snippet-data.sh /var/lib/docker/data/extract/
							When these steps are completed, data is mounted to containers and is
								ready for use with Black Duck SCA. The next step is
								to install Black Duck SCA.

						

					
				

				
					Add the hostname and IP address of the KB endpoint to the
							bds.security.hostHeaderAllowlistCsv key in the
							overrides.properties file:

					cd /var/lib/docker/Orchestration/kb-orch/config
vi overrides.properties
					For example:

					bds.security.hostHeaderAllowlistCsv=127.0.0.1,mykb.organization.com
				

				
					Bring up KB Services.

					Go to the following folder and use the following commands to bring up the KB
						services:

					cd ~/software/Orchestration/kb-orch/
docker-compose -p hub -f docker-compose.onprem.yml up -d

				
					Validate services:

					To check if all KB services are up as expected, run docker ps command:

					docker ps
					Note: Ensure that the nginx container (blackducksoftware/kb_nginx) is running.
						This is the load balancer guiding your requests.
To verify this,
						open up a browser window from somewhere that can access the KB server, and
						type the following:

					http://<ip_address>/api/authentication-health
				

				
					Ensure specific ports are open.

					For the docker containers to communicate behind the load balancer, the
						following ports on that machine must be opened: 443, 8080, 80 and 5432,
						which enable communication between docker containers.


===== TOPIC: Installing Black Duck SCA =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id GTfaZsIXWk9sMkqDFc1q5Q)

This chapter describes the process for installing Black Duck SCA.

		The Black Duck Air-gapped KnowledgeBase Services are decoupled from the Black Duck SCA version. All Air-gapped KB
			versions can act as a single KB in a one-to-many Black Duck SCA instance model. Black Duck SCA
			recommends this model for optimal performance and ease of management; you can set up a
			separate VM for Black Duck SCA.

		The following instructions are to configure a Black Duck SCA instance isolated from the KB
			server, and to configure the Black Duck SCA instance on the same server as the KB server by
			following the steps described below on the KB server itself.

		Prerequisites

			
			The following are the system requirements to install Black Duck SCA:

			
				
					Downloaded artifacts

				

				
					Black Duck SCA license key (suite_v1.xml) from Black Duck
						Support

				

				
					Refer to the Black Duck Docker Swarm installation guide installation planning
						chapter for information about the requirements.

				

			
		

		Bringing up Black Duck SCA

			
			Apply the license key and start the Black Duck SCA system.:

			Note: You will need the suite_v1.xml file that Black Duck Support gave you to
				complete this process.

			
				
					Set up the Black Duck SCA images. For this step, the Docker daemon must be up and
						running.

					Ensure Docker is installed correctly; to verify, use the sudo docker
						ps command.

					
						
							Navigate to the Black Duck folder and load the Docker images by using the following
								commands.

							cd ~/software/Blackduck/
sh load_images.sh
							It's helpful to check if there are any existing images and containers loaded by using the following
									commands:

							docker images ls
docker container ls
						

					
				

				
					Apply the license key.

					
						
							If this is your first time setting up Black Duck SCA, use the following
								command to create a volume for the configuration:

								docker volume create hub_config-volume
						

						
							Use the docker ps command to verify that Black Duck SCA
								is down.

						

						
							Optional: If any containers are running, go to the
								docker-swarm folder and use the following command to bring down the
								containers:

							docker stack rm hub
						

						
							Go the the /var/lib/docker/volumes/hub_config-volume/_data/ directory and
								paste/overwrite the suite_v1.xml file that you get
								from Black Duck support by using the following
								commands:

							cd /var/lib/docker/volumes/hub_config-volume/_data/
rm suite_v1.xml
cp -p <path_to_suite_v1.xml> .
						

					
				

				
					Bring up the Black Duck SCA system.

					
						
							Optional: Go to the folder with the orchestration files and
								edit the hub-webserver.env file in the
								docker-compose directory and configure a hostname of your choosing
								as shown in the following example:

							PUBLIC_HUB_WEBSERVER_HOST=mysca.organization.com

						

						
							Go back to the orchestration folder and edit the
								blackduck-config.externalHub.env file using a
								text editor such as Vim.

							cd ~/software/Orchestration/hub-*/docker-swarm/
vi blackduck-config.externalHub.env
						

						
							Replace the IP Address of On Prem KB with the IP
								address or hostname of your KB server and save the file.

							Note: Ensure this matches either the hostname or IP address of the value
								set for bds.security.hostHeaderAllowlistCsv in the
									overrides.properties file.

						

						
							Copy all contents from
								blackduck-config.externalHub.env and overwrite
								the blackduck-config.env file with the new updated
								instructions.

							cd ~/software/Orchestration/hub-*/docker-swarm/
docker swarm init
docker stack deploy -c docker-compose.yml hub
						

						
							Optional: In addition to Black Duck SCA, if you want to scan using
								BDBA (Black Duck Binary Analysis), use the following command:

							
								docker stack deploy -c docker-compose.yml -c docker-compose.bdba.yml hub
							

							Tip: Repeat the above steps for all instances of Black Duck SCA servers you want to
								create.

						

					
					Note: All containers except kb-meta-api, kbapi-snippet-lookup
						and kb_search should show a status of “Healthy”. When you
						use Docker Swarm, containers might take a few minutes to come up.

				

			
			Upon startup, verify that Black Duck SCA is accessible by typing https://<hostname>;
				if prompted with an invalid registration message, enter the root node text from your
				suite_v1.xml file, for example, as follows:

			example_hub_8002H000002PyifQAC


===== TOPIC: Frequently Asked Questions =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id 9d3WCTl37QSAtZVhOZ7kbw)

This chapter answers frequently asked questions.

		Question: How do I work with tmux?

			
			Answer: Tmux is a Linux utility that keeps a terminal session running, which
				helps in taking care of long running processes. This can prove helpful in deployment
				scripts and data extraction processes.

			To start a tmux session named “sample”, type the following command:

			tmux new -s sample
			You should see a terminal window with a green bar below it. Whatever command you run
				here runs in the background when you detach from it. This enables multiple
				extractions in parallel. To detach from that session use the following keys:

			“Ctrl+B” followed by “D”

			To check on progress/ attach to container again, use the following:

			
				tmux attach-session -t sample
			

		

		Question: How do I upgrade data released on a monthly basis?

			
			Answer: In the Black Duck Air-gapped KnowledgeBase, the volumes for the KnowledgeBase
				data and your Black Duck SCA instance are separate. To update old
				data with the new data set, use the following commands in accordance to your
				system.

			
				
					Navigate to the docker-compose folder, bring down the docker containers and
						list the docker volumes using the following commands:

					cd ~/software/Orchestration/hub-*/docker-swarm/
docker stack rm hub
docker volume ls
					Note: 
						Note down any volumes with the prefix “kb_” as these
							volumes are for the KB services.

					

				

				
					Using the docker volume rm command to remove the associated
						volumes. To remove match data, api data, solr data use the following
						command:

					
						docker volume rm -f kb_pg_api kb_api_snippet
					

					When the volumes are removed, which might take a while, expect to see some
						space free up on your mounted device.

				

				
					Copy the new data for the new month; refer to steps in Chapter 2 for copying
						data.

					
						
							Copy over data, extract it, use the create and mount scripts, and
								mount into the database containers.

						

					
				

				
					Bring the docker containers up for the on-premise system using a command
						similar to the following:

					
						docker stack deploy -c docker-compose.yml -c docker-compose.bdba.yml hub
					

				

			
		

		Question: How do I update the software only?

			
			Answer: To ensure that the volumes are maintained, do not use any docker
				volume commands in this procedure.

			Note: 
				The assumption is that a software update with changes to the KB services and Black Duck SCA are coming being consumed.

			

			
				
					Go to the docker-compose folder and bring down the containers.

					cd ~/software/Orchestration/hub-*/docker-swarm/docker stack rm hub
				

				Optional: You can remove the images from docker on your system as
						well.docker images
docker rmi <image_id>The docker images command returns an
						image id, which is associated with either a Black Duck SCA
						instance, or a KB service.
Note: Be careful with removing anything that
						indicates the possibility of the image being a database holder, for example,
							blackducksoftware/kb_api_db (note anything that
						ends with “db”).

				
					When the containers are down, place the new artifacts into the software
						folder and follow instructions to bring docker containers up in Chapter
						3.

				

				
					Go to the docker-compose folder and bring up the containers for Black Duck SCA and KB Services by using the following
						commands:

					cd ~/software/Orchestration/hub-*/docker-swarm/
docker stack deploy -c docker-compose.yml -c docker-compose.bdba.yml hub
					The correlation between the volume mount and where you extract data can be
						changed. Ensure that you modify the location in the
							docker-compose.onprem.externalHub.yml file


===== TOPIC: Updating and upgrading =====
# URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/ (topic id UQApKkL5fRFvKZoaFAJhng)

Use the command below to change the helm config values or to upgrade KB to latest version
			of the Black Duck Air-gapped KnowledgeBase:

		
					
						
							envsubst < values.yaml | helm upgrade kb . -n ${NAMESPACE} -f
								-
