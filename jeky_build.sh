cd new_website
jekyll build
rm /var/www/html/*
cp -r _site/* /var/www/html/
