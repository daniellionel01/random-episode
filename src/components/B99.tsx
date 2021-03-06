import episodes from "../data/b99.json"

export default function B99() {
  const index = Date.now() % episodes.length
  const season = Math.floor(index)

  const index2 = Date.now() % episodes[season].length
  const episode = Math.floor(index2)

  const ep = episodes[season][episode]

  return (
    <div>
      <h1><u>Brooklyn 99</u></h1>
      <div id="episode">
        S{season+1} E{episode+1}
      </div>
      <a href={`https://www.netflix.com/watch/${ep.id}`} target="_blank" id="link">
        {ep.title}
      </a>
    </div>
  )
}
