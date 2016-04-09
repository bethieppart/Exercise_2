
STEPS TO RUN EX2:
-----------------
1. Launch AWS EC2 instance using UCB W205 Spring Ex 2 Image (ami-4cf9f826)
2. Change to python 2.7 environment: source /opt/py27environment/bin/activate
2. Attach a volume already prepared per previous labs and exercises
3. Clone submitted Exercise_2 repository from Github: git clone <repository URL>
4. Change to Exercise_2 directory: cd Exercise_2
5. Make the db_setup script executable: chmod a+x db_setup.sh
6. Execute the setup script: bash db_setup.sh
7. Change to the EX2Tweetwordcount directory: cd EX2Tweetwordcount
8. Run the application: sparse run
9. When you see a word count reach 10 stop the application with ^C
10. Run finalresults.py with no argument: python finalresults.py
11. Run finalresults.py with a common word argument: python finalresults.py the
12. Run histogram.py to see all the words with counts between 6-10: python histogram.py 6,10
