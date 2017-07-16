
var acct = new Vue({
  el: '#acct',
  delimiters: ['[[', ']]'],
  data: {
    user: 'admin',
    pwd: 'password'
},
  methods: {
    fetchHelloWorld: function(){
      fetch('http://127.0.0.1:8000/api/hello-viewset/?format=json',{
        method:'GET'
      })
      .then(response => response.json())
      .then(json => console.log(json))
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
    postNewHabit: function() {
      fetch("http://127.0.0.1:8000/api/habit/", {
      method: "post",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
       'Authorization': 'Token '+this.authToken.token
      },
      credentials: 'include',

      //make sure to serialize your JSON body
      body:  JSON.stringify({ "habit": "Meditation", "count": 15,
      "checked_date": "2017-07-12", "start_date": "2017-07-07",
      "active_habit": false })

    })
    .then( (response) => {
       //do something awesome that makes the world a better place
       console.log(response);
     });
   },
   login: function() {
     fetch("http://127.0.0.1:8000/api/login/", {
     headers: {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
     },
     method: "POST",
     //make sure to serialize your JSON body
     body:  JSON.stringify({ username: 'test2',
                  password: 'testpassword' })
      }).then(response => response.json())
    .then(json => authToken = json)
    .then(console.log(authToken))
    .then(localStorage.setItem("token",this.authToken.token))
    }
  }
})
