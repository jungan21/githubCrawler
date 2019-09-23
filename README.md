# Prerequisite 
1. install Python first :)
2. run `pip install Scrapy` to intall Scrapy dependency



# How to run 
Suppose we are going to check whether any files under the following  github repo fold contain any senstive info: 

`https://github.com/ditclear/MVVM-Android/tree/bfbbc4536e057f16bde923f8676c2befa6a47321/app/src/main/res/values`

This fold includes 3 files: `colors.xml`, `strings.xml`, `styles.xml`

1. check out the code: `git clone https://github.com/jungan21/githubCrawler.git`
2. `cd githubCrawler/githubCrawler`
3. run command: (pass the above URL to git repo file fold to `urls` variable in below command) 

`scrapy crawl example -a urls=https://github.com/ditclear/MVVM-Android/tree/bfbbc4536e057f16bde923f8676c2befa6a47321/app/src/main/res/values`

4. Sample output:



<==== Start Checking Sensitive Information for file: styles.xml ===>

FOUND SENSITIVE Information: colorPrimary in file styles.xml

<=== End Checking Sensitive Information for file: styles.xml ===>

....
....

<=== Start Checking Sensitive Information for file: colors.xml ===>

FOUND SENSITIVE Information: colorPrimary in file colors.xml

<=== End Checking Sensitive Information for file: colors.xml ===>


<=== Start Checking Sensitive Information for file: strings.xml ===>

Safe!

<=== End Checking Sensitive Information for file: strings.xml ===>
