//function myFun() {
     //       document.getElementById("demo")
      //          .innerHTML = "Vehicle Registered Successfully";
      //  }
//function myFun() {
 //  window.alert("Vehicle registered successfully")}


 //var form = document.getElementById('form')
 var form = document.querySelector('form')
 form.addEventListener('submit', function(even){
   event.preventDefault()

   var fname = document.getElementById('fname').value
   var lname = document.getElementById('lname').value
   var age = document.getElementById('age').value
   var mname = document.getElementById('mname').value
   var myear = document.getElementById('myear').value
   var mdate = document.getElementById('mdate').value


   var formData = new FormData(form)
   var data = Object.fromEntries(formData);
   var jsonData = JSON.stringify(data);

   console.log(fname)
   console.log(lname)
   console.log(age)
   console.log(mname)
   console.log(myear)
   console.log(mdate)
   console.log(jsonData)

})


