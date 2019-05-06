<template>
  <div>
    <div class="container">
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
      currentTags: "",
      results: [
        { top: "top1", title: "title1", text: "text1" },
        { top: "top2", title: "title2", text: "text2" },
        { top: "top3", title: "title3", text: "text3" }
      ]
    };
  },

  methods: {
    search() {
      const path = "http://0.0.0.0:5057/news";
      axios.defaults.headers.post["Content-Type"] =
        "application/json;charset=utf-8";
      axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
      axios
        .get(path, { params: { tags: this.currentTags.split(" ") } })
        .then(response => {
          this.results = response.data["result"];
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>