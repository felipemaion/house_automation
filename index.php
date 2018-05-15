<!DOCTYPE html>
<html lang="en">

  <head>
    <head>
      <title>Automatização Residencial</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
      <script defer src="https://use.fontawesome.com/releases/v5.0.8/js/all.js" integrity="sha384-SlE991lGASHoBfWbelyBPLsUlwY1GwNDJo3jSJO04KZ33K2bwfV9YBauFfnzvynJ" crossorigin="anonymous"></script>
      <link rel="stylesheet" href="grid.css">

          <script>
      $(document).ready(function(){
          $('.btn').click(function(){
            $('.btn').load('swap.php', {'device':this.name});
            // alert(this.name);
            location.reload();
          });
      });
    </script>
    </head>





    <body>


    <div class="container-fluid">
      <br>
      <?php $umid_temp = exec("python3 get_temp_umid.py &"); ?>
      <?php $umid_temp = explode(',', $umid_temp); ?>
      <center><h4> Temperatura: <?=$umid_temp[0]?>˚C</h4>
      <h4> Umidade: <?=$umid_temp[1]?>% </h4></center>
      <br>

      <center>
    
      <?php 
        $data = exec("python3 getstatus.py &");
        // Removing the outer list brackets
        $data =  substr($data,1,-1);

        $myArr = array();
        // Will get a 3 dimensional array, one dimension for each list
        $myArr =explode('],', $data);

        // Removing last list bracket for the last dimension
        if(count($myArr)>1)
        $myArr[count($myArr)-1] = substr($myArr[count($myArr)-1],0,-1);

        // Removing first last bracket for each dimension and breaking it down further
        foreach ($myArr as $key => $value) {
        $value = substr($value,1);
        $myArr[$key] = array();
        $myArr[$key] = explode(',',$value);
        }
        ?>
        <!-- Put the data in the buttons -->
        <div class="row">
        <?php 
        $count = 0;
            foreach ($myArr as list($pin, $io, $description,$state,$high,$on_off, $name)) 
            {


              
                echo '<div class="col">';
                  echo '<button name='.$name.' type="button" class="btn btn-device">';
                  echo '<span class="fa fa-lightbulb '.$on_off.'"></span>';
                  echo '<span class="fa-class"> '.$description.' </span>';
                echo '</div>';
                $count += 1;
                if ($count == 2) {
                  echo '<div class="w-100"></div>';
                  $count = 0;
                }

            }
        ?>
        </div>
    </center>
      <br>

      <br>
   
    </div>
    
    </body>

</html>
