import React from "react";
import { render } from "react-dom";
import axios from "axios";
import TaskDescription from "./TaskDescription";

const SEARCH_ENDPOINT = "https://api.github.com/search/repositories?q=";

const getReactRepositories = (name) =>
  axios
    .get(SEARCH_ENDPOINT + name)
    .then((result) => result.data.items)
    .then((repos) =>
      repos.map(({ forks, name, stargazers_count, html_url }) => ({
        forks,
        name,
        stars: stargazers_count,
        url: html_url,
      }))
    );
let timeId = null;
class Solution extends React.Component {
  state = {
    value: "react",
    data: [],
  };

  onChange(e) {
    this.setState(
      {
        value: e.target.value,
      },

      async () => {
        if (timeId) {
          clearTimeout(timeId);
        }
        timeId = setTimeout(async () => {
          const data = await getReactRepositories(this.state.value);
          console.log(data);
          this.setState({
            data,
          });
        }, 500);
        if (timeId) {
          // clearTimeout(timeId);
        }
      }
    );
  }

  render() {
    return (
      <div>
        <h2>Search</h2>
        <input value={this.state.value} onChange={this.onChange.bind(this)} />
        <ul>
          {this.state.data.map((repo, i) => (
            <li key={i}>
              {repo.name} - 🌟 {repo.stars} - 🍴 {repo.forks}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

const App = () => (
  <div>
    <TaskDescription />
    <Solution />
  </div>
);

render(<App />, document.getElementById("root"));
