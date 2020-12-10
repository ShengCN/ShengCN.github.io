cd new_website
jekyll build
rm -r /var/www/html/*
cp -r _site/* /var/www/html/
