# tlg
sudo apt-get install imagemagick
https://itsfoss.com/convert-multiple-images-pdf-ubuntu-1304/

in /etc/ImageMagick-7/policy.xml
right before </policymap>
add 
<policy domain="coder" rights="read | write" pattern="PDF" />
https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion



