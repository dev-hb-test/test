<?php require_once('config.php'); 

$last = $conn->query("SELECT * FROM hafid ORDER BY id DESC LIMIT 1")->fetch_array();

?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hafid Moul Buvet</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <meta name="description" content="Jiw 3andi l buvet, lahaj li bghitoha mojoda">
<style>
    body{
        background-image : url('https://cutewallpaper.org/21/discord-backrounds/Quickly-remade-the-new-discord-invite-background-discordapp.jpg');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }
</style>
</head>
<body class="bg-dark text-light">

    <div class="text-center mt-2">
        
        <?php
            if(isset($_GET['q'])){
                if($_GET['q'] == "ok") echo "<h1 class='mt-2 text-success'>Help Hafid understand the world</h1>";
                else echo "<h1 class='mt-2 text-danger'>Help Hafid understand the world</h1>";
            }else echo "<h1 class='mt-2'>Help Hafid understand the world</h1>";
        ?>
        <p style="color: #ccc">Take a minute and help hafid understand the other members on the server</p>
        
        <hr />
        
        <div class="d-md-flex flex-row">
        
        <div class="d-flex flex-column justify-content-center col-md-4 text-left bg-transparent border-0">
            <h3>Last inserted row by <?= $last['name'] ?></h3>
            
            <br />
            
            <label for="p_question"><b>Question</b></label>
            <span id="p_question">--> <?= $last['question'] ?></span>
            
            <br />
            
            <label for="p_answer"><b>Answer</b></label>
            <span id="p_answer">--> <?= $last['answer'] ?></span>
            
            <br />
            
            If someone called John asked that question, Hafid will answer by :<br />
            <?= str_replace("[name]", "John", $last['answer']) ?>
        </div>
        
        <div class="card col-md-4 text-left" style="border-radius:12px;background-color: #8e44ad">
            
            <div class="card-body">
                
                <div class="text-center mt-3 mb-3">
                    <img src="https://i1.wp.com/www.gamedesignnotes.com/wp-content/uploads/2018/05/Discord.png?fit=300%2C300&ssl=1" width=120>
                </div>
                
                <form action="insert.php" method="POST">
                    <div class='form-group'>
                        <label for="name">Name</label>
                        <input class="form-control" name="name" required value="<?= isset($_SESSION['name']) ? $_SESSION['name'] : '' ?>" placeholder="Your name here">
                    </div>
                    <div class='form-group'>
                        <label for="name">Question</label>
                        <input class="form-control" name="question" required placeholder="The question">
                    </div>
                    <div class='form-group'>
                        <label for="name">Answer</label>
                        <input class="form-control" name="answer" required placeholder="Provide an answer">
                        <p>
                           <small>
                               use [name] to put author name in the message
                           </small> 
                        </p>
                    </div>
                    
                    <div class='form-group'>
                        <button class="btn btn-outline-primary float-right text-light" name="do_insert">Insert</button>
                    </div>
                </form>
            </div>
        </div>
        
        </div>
        
    </div>
    
    <div class="text-center mt-5">
        Copyright @2020, All rights reserved <a href="https://devcrawlers.com/" target="_blank">DevCrawlers</a>
    </div>
    
</body>
</html>