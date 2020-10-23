import io from 'socket.io-client'

const socket = io('127.0.0.1:8000')

export default function createSocket(socket){
    return (store) => {
        socket.on('appointment', (data) => {
            store.commit('setAppointments', data)
        })
    }
}