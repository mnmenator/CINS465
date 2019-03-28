//var app = new Vue({
//  el: '#app',
//  data: {
//    message: 'Hello Vue!'
//  }
//})

//var app2 = new Vue({
//  el: '#app-2',
//  data: {
//    message: 'You loaded this page on ' + new Date().toLocaleString()
//  }
//})

//var app4 = new Vue({
//  el: '#app-4',
//  data: {
//    todos: [
//      { text: 'Learn JavaScript' },
//      { text: 'Learn Vue' },
//      { text: 'Build something awesome' }
//    ]
//  }
//})

var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: [],
    seen: true,
    unseen: false
  },

  created: function() {
    this.fetchTodoList();
    this.timer = setInterval(this.fetchTodoList, 10000);
  },
  methods: {
    fetchTodoList: function() {
      axios
        .get('/todos/')
        .then(response => (this.todos = response.data.todos))
      console.log(this.todos)
      this.seen=false
      this.unseen=true
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }

})
