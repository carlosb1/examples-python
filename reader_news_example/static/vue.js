// TODO make info an IIFE
// TODO make into Vue.component
new Vue({
    el: '#contact_form', // id of the 'app'
    data: {
        link: '',   // data for the name on the form
    },
    methods: { // all the actions our app can do
        isValidLink: function () { // TODO what if name is just spaces?
            var valid = (this.link.length > 0) && (this.link.startWith('http://') == true || this.link.startWith('https://') == true);
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
	    xhr.send(data);
        }
    }
});
