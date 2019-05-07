<template>
  <div>
    <div class="container">
      <div>
        <br>
        <h5>Add new link</h5>
        <hr>
        <br>
        <b-btn href="#" v-b-toggle.accordion_add_url variant="primary">Add URL</b-btn>
        <b-collapse id="accordion_add_url" role="tabpanel">
          <!-- some content -->
          <div class="input-group p-4 row">
            <div class="col-10">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">URL:</span>
                </div>
                <input
                  v-model="currentURL"
                  type="text"
                  class="form-control"
                  id="basic-url"
                  aria-describedby="basic-addon3"
                >
              </div>
            </div>
            <div class="col-2">
              <span class="input-group-btn">
                <button class="btn btn-primary" type="button" v-on:click="addURL()">add!!</button>
              </span>
            </div>
          </div>
        </b-collapse>
      </div>

      <div v-if="results">
        <hr>
        <div class="msg-group p-2" v-for="elem in results">
          <div class="card">
            <div class="card-header">{{ elem.top }}</div>
            <div class="card-body">
              <h5 class="card-title">{{ elem.title }}</h5>
              <p class="card-text">{{ elem.text}}</p>
              <a href="#" class="btn btn-primary">More information</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      currentURL: "",
      results: [
        { top: "top1", title: "title1", text: "text1" },
        { top: "top2", title: "title2", text: "text2" },
        { top: "top3", title: "title3", text: "text3" }
      ]
    };
  },

  methods: {
    get() {
      const path = "http://0.0.0.0:5057/news";
      axios
        .get(path, { params: { tags: this.currentTags.split(" ") } })
        .then(response => {
          // TODO ADD PARSER
          this.results = response.data["result"];
        })
        .catch(error => {
          console.log(error);
        });
    },
    search() {
      const path = "http://0.0.0.0:5057/news/search";
      axios
        .get(path, { params: { tags: this.currentTags.split(" ") } })
        .then(response => {
          // TODO ADD SEARCH
        })
        .catch(error => {
          console.log(error);
        });
    },
    addURL() {
      const path = "http://0.0.0.0:5057/urls";
      axios
        .post(path)
        .then(() => {
          //TODO add urls
        })
        .catch(error => {
          //TODO add errors
        });
    }
  }
};
</script>