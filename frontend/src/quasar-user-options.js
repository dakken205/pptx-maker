
import 'quasar/dist/quasar.css'
import '@quasar/extras/material-icons/material-icons.css'
import { Loading} from 'quasar'

// To be used on app.use(Quasar, { ... })
export default {
  config: {
    loading: {
      message: 'Processing your request...'
    }
  },
  plugins: {
    Loading
  }
}