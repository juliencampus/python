import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    appointments:{}
  },
  mutations: {
    setAppointments(state, payload){
      state.appointments = payload
    }
  },
  actions: {
    getAppointments({ commit }){
      var config = {
        // headers: {
          "Access-Control-Allow-Origin": "*",
        //   "Access-Control-Allow-Credentials": "true",
        //   "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
        //   "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers,access-control-allow-origin",
        //   // 'Content-Type': 'application/json',
        // }
      };
      axios
        .get('http://127.0.0.1:8000/appointments', config)
        .then(res => {
          let apnts = res.data 
          console.log(apnts)   
          commit('setAppointments', apnts)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  modules: {
  }

})
