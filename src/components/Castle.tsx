import episodes from "../data/castle.json"

export default function Friends() {
  const index = Date.now() % episodes.length
  const season = Math.floor(index)

  const index2 = Date.now() % episodes[season].length
  const episode = Math.floor(index2)

  const ep = episodes[season][episode]

  return (
    <div>
      <h1><u>Castle</u></h1>
      <div id="episode">S{season+1} E{episode+1}</div>
      <a href={`https://www.disneyplus.com/video/${ep.id}`} target="_blank" id="link">
        {ep.title}
      </a>
    </div>
  )
}
