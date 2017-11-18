// TODO make info an IIFE
// TODO make into Vue.component
var contact_form = new Vue({
    el: '#contact_form', // id of the 'app'
    data: {
        link: '',   // data for the name on the form
	news: []
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
        },
  	function save_to_data(my_grid_data) {
		this.news = my_grid_data;
  	},
       created: function () {
  	console.log('getting information...');
	    var xhr = new XMLHttpRequest();
	    var url = "http://localhost:5000/api/news";
	    xhr.open("GET",url,true);
	    xhr.setRequestHeader("Content-type", "application/json");
	    xhr.onreadystatechange = function () {
		if (xhr.readyState == 4 && xhr.status == 200) {
			var json = JSON.parse(xhr.responseText);
			var my_grid_data = [];
			for (var entry in json['objects']) {
				title_ = json['objects'][entry]['title'];
				link_ = json['objects'][entry]['link'];
				my_grid_data.push({link: link_, title: title_});
			}
			save_to_data(my_grid_data);
			//console.log(json);
		}
	    };
	    xhr.send();
  	}
    }
});

