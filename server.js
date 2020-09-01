// Simulates github pages

import express from 'express'
import fs from 'fs'
import util from 'util'
const readFile = util.promisify(fs.readFile)

const app = express()
app.get('/', async (req, res) => {
  const index = (await readFile('./index.html')).toString()
  res.send(index)
})
app.use('/emoticons', express.static('emoticons'))
app.get('/emoticons.json', async (req, res) => {
  const emoteJson = (await readFile('./emoticons.json')).toString()
  res.json(emoteJson)
})
app.listen(3024, () => {})
