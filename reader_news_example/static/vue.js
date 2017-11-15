// TODO make info an IIFE
// TODO make into Vue.component
var contact_form = new Vue({
    el: '#contact_form', // id of the 'app'
    data: {
        link: '',   // data for the name on the form
    },
    methods: { // all the actions our app can do
        isValidLink: function () { // TODO what if name is just spaces?
            var valid = (this.link.length > 0) && (this.link.startsWith('http://') == true || this.link.startsWith('https://') == true);
            console.log('checking for a valid link: ' + valid);
            return valid;
        },
        submitForm: function () {
            console.log('submitting message...');
	    var xhr = new XMLHttpRequest();
	    var url = "http://localhost:5000/api/news";
	    xhr.open("POST",url,true);
	    xhr.setRequestHeader("Content-type", "application/json");
	    xhr.onreadystatechange = function () {
		if (xhr.readyState == 4 && xhr.status == 200) {
			var json = JSON.parse(xhr.responseText);
			console.log(json);

		}
	    };
	    var data = JSON.stringify({"link": this.link});
	    /*clear form */
	    this.link = '';
	    xhr.send(data);
        }
    }
});

// register the grid component
Vue.component('demo-grid', {
  template: '#grid-template',
  props: {
    data: Array,
    columns: Array,
    filterKey: String
  },
  data: function () {
    var sortOrders = {}
    this.columns.forEach(function (key) {
      sortOrders[key] = 1
    })
    return {
      sortKey: '',
      sortOrders: sortOrders
    }
  },
  computed: {
    filteredData: function () {
      var sortKey = this.sortKey
      var filterKey = this.filterKey && this.filterKey.toLowerCase()
      var order = this.sortOrders[sortKey] || 1
      var data = this.data
      if (filterKey) {
        data = data.filter(function (row) {
          return Object.keys(row).some(function (key) {
            return String(row[key]).toLowerCase().indexOf(filterKey) > -1
          })
        })
      }
      if (sortKey) {
        data = data.slice().sort(function (a, b) {
          a = a[sortKey]
          b = b[sortKey]
          return (a === b ? 0 : a > b ? 1 : -1) * order
        })
      }
      return data
    }
  },
  filters: {
    capitalize: function (str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    }
  },
  methods: {
    sortBy: function (key) {
      this.sortKey = key
      this.sortOrders[key] = this.sortOrders[key] * -1
    }
  }
});

// bootstrap the demo
var demo = new Vue({
  el: '#demo',
  data: {
    searchQuery: '',
    gridColumns: ['link', 'Number of words'],
    gridData: [
      { name: 'Chuck Norris', power: Infinity },
      { name: 'Bruce Lee', power: 9000 },
      { name: 'Jackie Chan', power: 7000 },
      { name: 'Jet Li', power: 8000 }
    ]
  }
});
