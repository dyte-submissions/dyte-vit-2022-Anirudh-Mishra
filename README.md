[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7955175&assignment_repo_type=AssignmentRepo)
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SDK Dependency Updation Tool</h3>

  <p align="center">
    This project contains a python script that extracts mentioned repositories, checks the version of the mentioned dependencies by comparing them with the required versions and provides an option to update the dependencies to the required version if they are dated, thus generating a pull request with the updated dependency versions, automating and making it more convenient for the user.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project contains a python script that checks specified repositories for whether the specified dependencies satisfy specified version requirements by crawling the package.json and package-lock.json file. It produces an output file stating the validation of the satisfaction of each repository. Another feature of the project involves updation of the dependencies and creation of a pull request for the same and stating of the pull request link in an output file.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Node.js](https://nodejs.org/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

In order for the tool to work, it is mandatory that the repositories being worked upon belong to the user or contains the user as a collaborator in order for the tool to function appropriately. 

Given below are the libraries/packages required beforehand for smooth functioning of the tool/script along with their install command.
* npm
  ```sh
  npm install npm@latest -g
  ```

* typer
  ```sh
  pip install typer
  ```

* python-git
  ```sh
  pip install python-git
  ```
  
* os
  ```sh
  pip install os
  ```
  
* glob
  ```sh
  pip install glob
  ```
  
* json
  ```sh
  pip install json
  ```

* requests
  ```sh
  pip install requests
  ```
  
* subprocess
  ```sh
  pip install subprocess
  ```

* PyGithub
  ```sh
  pip install github
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Anirudh-Mishra/dyte-vit-2022-Anirudh-Mishra.git)
   ```
2. Install NPM and python packages as mentioned in prerequisite section
   ```sh
   npm install <package_name>
   pip install <package_name>
   ```
3. Generate a personal github access token by navigating to Setting>Developer Options>Personal Access Tokens. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


1. Create a CSV file by a custom name <data_file_name> containing two columns namely, the repository name and the repository link.

2. Open terminal/cmd on your desktop and navigate to the directory of the cloned project.

3. Type the following command if you just want an intimation as to which repositories do not match the requirement of the stated version of a dependency
   ```sh
   python ./index.py <data_file_name>.csv <dependency_name>@<required_version> --no-update
   ```
   If you want to further create a pull request for updation proceed to further steps.
   
4. Type the following command if you want to create a pull request of the updation changes of the stated dependency to required version
   ```sh
   index <data_file_name>.csv <dependency_name>@<required_version> --update
   ```
   
5. Go to the repositories that you created to check whether a new branch by the name 'updated-branch' has been created in case of inadequate dependency versions to        mark the success of required changes.

6. Go to the pull requests section in the repository. A newly formed pull request denotes success of the procedure and can be merged as and when required!


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Crawl through repositories to detect specified dependency versions
- [x] Write the validity of the dependency versions with respect to the required specified versions to an output file
- [x] Update the version of the required dependecies in the desired repository clones
- [x] Create a pull request on a public as well as private repository belonging to the user

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Anirudh Mishra - [Anirudh30502](https://twitter.com/Anirudh30502) - mishraanirudhmail@gmail.com

Project Link: [https://github.com/Anirudh-Mishra/dyte-vit-2022-Anirudh-Mishra](https://github.com/Anirudh-Mishra/dyte-vit-2022-Anirudh-Mishra)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
