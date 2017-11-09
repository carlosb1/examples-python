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
            this.$http({url: '/someUrl', method: 'POST', data: {
                link: this.link,
            }}).then(function () {
                alert('Your form was submitted!');
            }, function () {
                alert('Form submission failed');
            });
        }
    }
});
