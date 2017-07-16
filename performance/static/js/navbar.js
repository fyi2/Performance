let vmNavbar = new Vue({
 el: '#navbar',
 delimiters: ['[[', ']]'],
 data: {
  message: "hi there :)",
  habits: [0,0,0,0,0],
  temp: 0,
  disabled: [false,false,false,false,false]
},
methods: {
  seinfeld: function(habit){
    temp = this.habits[habit] +1;
    Vue.set(vm.habits,habit,temp);
    Vue.set(vm.disabled,habit,true);
    return this.habits[habit]
    }
  },
  fetchHabits: function() {
    console.log('Token '+this.authToken.token);
    fetch('http://127.0.0.1:8000/api/habit/?format=json',{
       method: 'GET',
       headers: {
         'Accept': '*/*',
         'Content-Type': 'application/json',
         'Authorization': 'Token '+this.authToken.token
       },
       credentials: 'include'
    })
  .then(response => response.json())
  .then(json => this.habits = json)
  },
});
