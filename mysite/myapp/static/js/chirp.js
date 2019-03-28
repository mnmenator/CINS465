var app4 = new Vue({
  el: '#chirp-app',
  data: {
    chirps: [],
    seen: true,
    unseen: false
  },

  created: function() {
    this.fetchChirpList();
    this.timer = setInterval(this.fetchChirpList, 10000);
  },
  methods: {
    fetchChirpList: function() {
      axios
        .get('/chirps/')
        .then(response => (this.chirps = response.data.chirps))
      console.log(this.chirps)
      this.seen=false
      this.unseen=true
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }

})
