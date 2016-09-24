usage(){
	echo "USAGE:"
	echo ""
	echo "  wget-all <url>        (retrieves all files for a website)"
	echo ""

	exit
}


if [ $# -ne 1 ]; then
	usage
fi

wget -r --no-parent $1
