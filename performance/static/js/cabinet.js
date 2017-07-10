new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    isActive: false,
    myTagInput: '',
    currentTag: '',
    delTag: ''

  },
  methods: {
    turnGreen: function(event) {
      element = event.currentTarget;
      id = element.getAttribute('id');
      this.isActive = id;
    },
    turnBlack: function() {
      this.isActive = false;
    },
    grabTag: function(delTag,tagID) {
      if (this.currentTag.length == 0){
        this.currentTag = delTag
      } else {
        this.currentTag = this.currentTag+','+delTag
      }
      var parent = document.getElementById("tags");
      var child = document.getElementById(tagID);
      parent.removeChild(child);

    }

  }
})
