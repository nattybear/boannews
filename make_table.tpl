<!DOCTYPE html>
<html>

<head>

<title>Security News Monitoring System</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="30">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
  (adsbygoogle = window.adsbygoogle || []).push({
    google_ad_client: "ca-pub-6112909469927816",
    enable_page_level_ads: true
  });
</script>

<style>
a:link {
	background-color: transparent;
	text-decoration: none;
}
a:visited {
	color: gray;
}
</style>

</head>

<body>

<div class="w3-container">

<table class="w3-table w3-striped">

%for row in rows:
	<tr>
		<td>{{row[3][5:16]}}</td>
		<td>{{row[0]}}</td>
		<td><a href="{{row[2]}}" target="_blank">{{row[1]}}</a></td>
	</tr>
%end
</table>

</body>
</html>
