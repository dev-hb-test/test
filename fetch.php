<?php

require_once 'config.php';

if(isset($_GET['action'])){
    if($_GET['action'] == "getall"){
        $rs = $conn->query("SELECT * FROM hafid");
        echo json_encode($rs->fetch_all(MYSQLI_ASSOC));
    } else echo json_encode([]);
} else echo json_encode([]);

exit;