import Vue from 'vue'
import {
    Button,
    Input,
    Form,
    FormItem,
    Message,
    MessageBox,
    Menu,
    MenuItem,
    Submenu,
    Container,
    Aside,
    Header,
    Main,
    Table,
    TableColumn
} from 'element-ui'
Vue.use(Button)
Vue.use(Input)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Submenu)
Vue.use(Container)
Vue.use(Aside)
Vue.use(Header)
Vue.use(Main)
Vue.use(Table)
Vue.use(TableColumn)
Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm