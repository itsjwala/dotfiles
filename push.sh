git add --all

msg="update"

if [ "$*" ] ; then
msg=$*
fi


git commit -m "$msg"

git pull origin master
git push origin -u master