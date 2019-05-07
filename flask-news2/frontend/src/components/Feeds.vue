<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Feeds</h1>
        <hr>
        <br>
        <br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.feed-modal>Add Source</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">URL</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(feed, index) in feeds" :key="index">
              <td>{{ feed.url }}</td>
              <td>
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.feed-update-modal
                  @click="editFeed(feed)"
                >Update</button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteFeed(feed)"
                >Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addFeedModal" id="feed-modal" title="Add a new feed" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addFeedForm.url"
            required
            placeholder="Enter URL"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editFeedModal" id="feed-update-modal" title="Update" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group" label="Title:" label-for="form-title-edit-input">
          <b-form-input
            id="form-title-edit-input"
            type="text"
            v-model="editForm.url"
            required
            placeholder="Enter URL"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert";

export default {
  data() {
    return {
      feeds: [],
      addFeedForm: {
        url: ""
      },
      editForm: {
        item_id: "",
        url: ""
      },
      message: "",
      showMessage: false,
      httpEndpoint: "http://0.0.0.0:5057/feeds" //process.env.ROOT_API
    };
  },
  components: {
    alert: Alert
  },
  methods: {
    getFeeds() {
      this.feeds = [
        { url: "my_url1", item_id: "1x" },
        { url: "my_url2", item_id: "2x" }
      ];
      /*
      const path = httpEndpoint;
      axios
        .get(path)
        .then(res => {
          this.feeds = res.data.feeds;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
        */
    },
    addFeed(payload) {
      /*
      const path = httpEndpoint;
      axios
        .post(path, payload)
        .then(() => {
          this.getFeeds();
          this.message = "Feed added!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getFeeds();
        });
      */
      this.getFeeds();
    },
    updateFeed(payload, feedID) {
      /*
      const path = `${this.httpEndpoint}/${feedID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getFeeds();
          this.message = "Feed updated!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getFeeds();
        }); */
      this.getFeeds();
    },
    removeFeed(feedID) {
      /*
      const path = `${this.httpEndpoint}/${feedID}`;
      axios
        .delete(path)
        .then(() => {
          this.getFeeds();
          this.message = "Feed removed!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getFeeds();
        });
        */
      this.getFeeds();
    },
    initForm() {
      this.addFeedForm.url = "";
      this.editForm.item_id = "";
      this.editForm.url = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addFeedModal.hide();
      let read = false;
      if (this.addFeedForm.read[0]) read = true;
      const payload = {
        feeds: [this.addFeedForm.title]
      };
      this.addFeed(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editFeedModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        feeds: [this.editForm.url]
      };
      this.updateFeed(payload, this.editForm.item_id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addFeedModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editFeedModal.hide();
      this.initForm();
      this.getFeeds(); // why?
    },
    onDeleteFeed(feed) {
      this.removeFeed(feed.item_id);
    },
    editFeed(feed) {
      this.editForm = feed;
    }
  },
  created() {
    this.getFeeds();
  }
};
</script>
