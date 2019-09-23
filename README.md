
# Github Repository Fold Crawler for Senstive Keywords

A Python tool to crawl all files under a GitRepo fold to identify the senstive keywords.

Currently, some keywords are hardcoded in the the file: [sensitive_word.txt](githubCrawler/sensitive_word.txt), please feel free to update the list to add/remove the senstive words you are interested.

# Setup

1 install Python3 on your machine

    instruction: https://docs.python.org/3/using/index.html
    
2 run `pip install Scrapy` to intall Scrapy dependency

3 Clone this repository by entering

    git clone https://github.com/jungan21/githubCrawler.git

4 Navigate to the githubCrawler directory

    cd githubCrawler/githubCrawler
    
    pwd (I'm on Mac OS, please make sure you are in this fold)
    -rw-r--r--  1 <SID>  ***\Domain Users   294 21 Sep 21:06 pipelines.py
    -rw-r--r--  1 <SID>  ***\Domain Users  3611 21 Sep 21:06 middlewares.py
    -rw-r--r--  1 <SID>  ***\Domain Users  3150 21 Sep 21:07 settings.py
    -rw-r--r--  1 <SID>  ***\Domain Users   341 22 Sep 20:54 items.py
    -rw-r--r--  1 <SID>  ***\Domain Users    67 23 Sep 09:57 sensitive_word.txt

    https://github.com/ditclear/MVVM-Android/tree/bfbbc4536e057f16bde923f8676c2befa6a47321/app/src/main/res/values

# Usage

Suppose we are going to check whether any files under the following github repo fold contain any senstive keywords: 
      
     https://github.com/ditclear/MVVM-Android/tree/bfbbc4536e057f16bde923f8676c2befa6a47321/app/src/main/res/values

Run the following command to start the crawler: (set urls=<link to the github repo fold>)

     scrapy crawl example -a urls=https://github.com/ditclear/MVVM-Android/tree/bfbbc4536e057f16bde923f8676c2befa6a47321/app/src/main/res/values


# Sample output:

This tool will scan/check file by file. i.e. for each file scan for the keywords you put in the [sensitive_word.txt](githubCrawler/sensitive_word.txt)

    Sample terminal output:

    <==== Start Checking Sensitive Information for file: _styles.xml_ ===>

    FOUND SENSITIVE Information: colorPrimary in file styles.xml

    <=== End Checking Sensitive Information for file: styles.xml ===>

    ....
    ....

    <=== Start Checking Sensitive Information for file: colors.xml ===>

    FOUND SENSITIVE Information: colorPrimary in file colors.xml

    <=== End Checking Sensitive Information for file: colors.xml ===>

    ....
    ....
    
    <=== Start Checking Sensitive Information for file: strings.xml ===>

    Safe!

    <=== End Checking Sensitive Information for file: strings.xml ===>
