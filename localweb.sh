#!/usr/bin/env bash
 
statusmsg(){
    if [ $1 == "pysimple" ]; then
        echo "Simple Web Server, using Python"
    fi
 
    if [ $1 == "pycgi" ]; then
        echo "Simple Web Server w/ CGI Support, using Python"
    fi
 
    if [ $1 == "php" ]; then
        echo "Simple Web Server, using PHP"
    fi
 
    if [ $1 == "phprem" ]; then
        echo "Simple Web Server, using PHP, with remote access"
    fi
 
    echo "(Ctrl-C to exit the running server.)"
    echo ""
}
 
usage(){
    echo "USAGE:"
    echo ""
    echo "  localweb <server_type> <port_number>"
    echo ""
    echo "  where <server_type> is one of the following:"
    echo "    pysimple    Starts a simple web server, using Python"
    echo "    pycgi       Starts a simple web server, with CGI support, using Python"
    echo "    php         Starts a simple web server, using PHP"
    echo "    phprem      Starts a simple web server, using PHP, with remote access"
    echo ""
    echo "e.g.: 'localweb pycgi 81' starts a simple web server with CGI support, using Python, listening on port 81."
 
    exit
}
 
if [ $# -ne 2 ]; then
    usage
fi
 
if [ $1 == "pysimple" ]; then
    statusmsg $1
    python -m SimpleHTTPServer $2
    exit
fi
 
if [ $1 == "pycgi" ]; then
    statusmsg $1
    python -m CGIHTTPServer $2
    exit
fi
 
if [ $1 == "php" ]; then
    statusmsg $1
    php -S localhost:$2
    exit
fi
 
if [ $1 == "phprem" ]; then
    statusmsg $1
    php -S 0.0.0.0:$2
    exit
fi
 
usage
