@ECHO OFF
ECHO ====== SOA UNIVERSITY ======
ECHO Auto pulling, adding, commiting and pushing on Github.
ECHO ===================================================================================

ECHO -------- Pulling --------
git pull
git status

ECHO -------- Adding --------
git add .
git status

ECHO -------- Commiting --------
git commit -m"updating classwork contents"

ECHO -------- Pushing --------
git push

ECHO ===================================================================================
ECHO Don't Have a Good Day, Have a Great Day
PAUSE