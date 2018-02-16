#!/usr/bin/php
<?php
function instagram_id_to_url($instagram_id){

	$url_prefix = "https://www.instagram.com/p/";

    if(!empty(strpos($instagram_id, '_'))){

        $parts = explode('_', $instagram_id);

        $instagram_id = $parts[0];

        $userid = $parts[1];

    }

    $alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
    $url_suffix = '';
    while($instagram_id > 0){

        $remainder = $instagram_id % 64;
        $instagram_id = ($instagram_id-$remainder) / 64;
        $url_suffix = $alphabet{$remainder} . $url_suffix;

    };

    return $url_prefix.$url_suffix;

}

// example
$insta_id = $argv[1];
echo instagram_id_to_url($insta_id);
echo "\n";
?>
