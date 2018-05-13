<!--
========================================
 Use (NUM)ON or (NUM)OFF in APPLICATION
========================================
ARVORE NATAL  MAP to PIN(GPIO)
abajur 1 pin7  (GPIO4)
OFF 2 pin11 (GPIO17)
OFF 3 pin12 (GPIO18)
OFF 4 pin13 (GPIO21)
OFF 5 pin15 (GPIO22)
OFF 6 pin16 (GPIO23)
OFF 7 pin18 (GPIO24)
OFF 8 pin22 (GPIO25)
-->

<?php 
if (isset($_POST['1ON']))
{
exec('python /home/pi/GPIO/automate.py 7 0');
}
if (isset($_POST['1OFF']))
{
exec('python /home/pi/GPIO/automate.py 7 1');
}
if (isset($_POST['2ON']))
{
exec('python /home/pi/GPIO/automate.py 11 0');
}
if (isset($_POST['2OFF']))
{
exec('python /home/pi/GPIO/automate.py 11 1');
}
if (isset($_POST['3ON']))
{
exec('python /home/pi/GPIO/automate.py 12 0');
}
if (isset($_POST['3OFF']))
{
exec('python /home/pi/GPIO/automate.py 12 1');
}
if (isset($_POST['4ON']))
{
exec('python /home/pi/GPIO/automate.py 13 0');
}
if (isset($_POST['4OFF']))
{
exec('python /home/pi/GPIO/automate.py 13 1');
}
if (isset($_POST['5ON']))
{
exec('python /home/pi/GPIO/automate.py 15 0');
}
if (isset($_POST['5OFF']))
{
exec('python /home/pi/GPIO/automate.py 15 1');
}
if (isset($_POST['6ON']))
{
exec('python /home/pi/GPIO/automate.py 16 0');
}
if (isset($_POST['6OFF']))
{
exec('python /home/pi/GPIO/automate.py 16 1');
}
if (isset($_POST['7ON']))
{
exec('python /home/pi/GPIO/automate.py 18 0');
}
if (isset($_POST['7OFF']))
{
exec('python /home/pi/GPIO/automate.py 18 1');
}
if (isset($_POST['8ON']))
{
exec('python /home/pi/GPIO/automate.py 22 0');
}
if (isset($_POST['8OFF']))
{
exec('python /home/pi/GPIO/automate.py 22 1');
}
?>

<title></title>
</head>
<body>
<form method="post">
<table style="width: 67%; text-align: left; margin-left: auto; margin-right: auto;"
 border="35" cellpadding="20" cellspacing="0">
 <center><font color="red" face="verdana" size="3">AUTOMACAO RESIDENCIAL</center>                  
</tr>
      </tr>
        <td style="text-align: center;">ABAJUR</td>
        <td style="text-align: center;"><button name="1ON">Ligado</button></td>
        <td style="text-align: center;"><button name="1OFF">Desligado</button></td>
      </tr>
      <tr>
        <td style="text-align: center;">OFF 2</td>
        <td style="text-align: center;"><button name="2ON">ON</button></td>
        <td style="text-align: center;"><button name="2OFF">OFF</button></td>
      </tr>
      <tr>
        <td style="text-align: center;">OFF 3</td>
        <td style="text-align: center;"><button name="3ON">ON</button></td>
        <td style="text-align: center;"><button name="3OFF">OFF</button></td>
      </tr>
      <tr>
        <td style="text-align: center;">OFF 4</td>
        <td style="text-align: center;"><button name="4ON">ON</button></td>
        <td style="text-align: center;"><button name="4OFF">OFF</button></td>
      </tr>
      <tr>
        <td style="text-align: center;">OFF 5</td>
        <td style="text-align: center;"><button name="5ON">ON</button></td>
        <td style="text-align: center;"><button name="5OFF">OFF</button></td>
      </tr>
      <tr>
        <td style="text-align: center;">OFF 6</td>
        <td style="text-align: center;"><button name="6ON">ON</button></td>
        <td style="text-align: center;"><button name="6OFF">OFF</button></td>
      </tr>
      <tr>
        <td style="text-align: center;">OFF 7</td>
        <td style="text-align: center;"><button name="7ON">ON</button></td>
        <td <font color="red"style="text-align: center;"><button name="7OFF">OFF</button></td>
      </tr>
      <td style="text-align: center;">OFF 8</td>
        <td style="text-align: center;"><button name="8ON">ON</button></td>
        <td style="text-align: center;"><button name="8OFF">OFF</button></td>
      </tr>
      <center><font color="blue" face="verdana" size="3">RASPBERRY PI 8 Canais</center>
      </tr>
      <center><font color="blue" face="verdana" size="3">SUPORTE: edsonroque26@gmail.com</center>
      <center><font color="red" face="verdana" size="4">WHATSAPP 12 981957154</center>
        </tr>
      
  </table>
</form>
</body>
</htm>
