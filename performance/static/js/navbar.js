let vm = new Vue({
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

}
});
