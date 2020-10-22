<template>
    <section>
        <v-form>
            <v-container>
                <v-text-field
                label="Nom"
                v-model="patientName"
                counter
                maxlength="40">
                </v-text-field>
                <v-select
                :items="items"
                item-text="name"
                item-value="val"
                :return-object="false"
                v-model="selectedDur"
                label="Nature de le rdv"
                solo>
                </v-select>
                <v-row>
                    <v-date-picker
                    v-model="date"
                    :allowed-dates="allowedDates"
                    class="mt-4"
                    min="2016-06-15"
                    max="2025-03-20"
                    ></v-date-picker>
                     <v-menu
        ref="menu"
        v-model="menu2"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="time"
        transition="scale-transition"
        offset-y
        max-width="290px"
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="time"
            label="Picker in menu"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="menu2"
          v-model="time"
          full-width
          format="24hr"
          min="08:00"
          max="17:30"
          @click:minute="$refs.menu.save(time)"
        ></v-time-picker>
      </v-menu>
                </v-row>
            </v-container>
              <v-btn
      color="success"
      class="mr-4"
      @click="validate"
    >
      Validate
    </v-btn>
        </v-form>
    </section>
</template>

<script>
import moment from 'moment'
import axios from 'axios'
export default {
    data: () => ({
        items: [
            {val: "0:30:00", name: "Simple (30')"}, 
            {val: "0:45:00", name:"Special (45')"},
            {val: "0:55:00", name:"Avec manipulation (55')"}
         ],
        date: null,
        time: null,
        menu2: false,
        selectedDur: false,
        patientName: ""
    }),
     methods: {
      allowedDates: val => moment(val).day() != 6 && moment(val).day() != 0,
    //   allowedHours: v => v > 8 && v < 18
      validate() {
        let params = {}
        params.duration = this.selectedDur
        params.starts_at = `${this.date} ${this.time}`
        params.patient = this.patientName
        axios.post('http://192.168.0.110/appointments/', params)
        .then(res =>{
            console.log(res)
            this.$router.push({name:'Index'})
        } )
        .catch(err =>{
            console.log(err)
            this.$router.push({name:'Index'})
        })
      }
    },
}
</script>

<style scoped>

</style>