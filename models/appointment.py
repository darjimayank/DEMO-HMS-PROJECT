from odoo import api, fields, models



class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'
   
  
    patient_id = fields.Many2one('hospital.patient',string='Patient') 
    gender = fields.Selection([('male', 'Male'),('female','Female')],string='gender', related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date',default=fields.Date.context_today) 
    ref = fields.Char(string = 'Reference')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref