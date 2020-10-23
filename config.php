<?php

session_start();

define("HOSTNAME", 'localhost');
define("USERNAME", 'root');
define("PASSWORD", '');
define("DBNAME", 'discord');

$conn = new mysqli(HOSTNAME, USERNAME, PASSWORD, DBNAME);
$conn->set_charset("utf8");
