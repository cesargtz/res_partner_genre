# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ResPartnerGenre(models.Model):
    _inherit = "res.partner"
    
    genre = fields.Selection(
        string='Genre',
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    
    def change_genre(self):
        for line in self:
            if line.genre == 'male':
                line.genre = 'female'
            elif line.genre == 'female':
                line.genre = 'male'
            else:
                raise exceptions.ValidationError("Genre not established")
    
    def write(self,values):
        res = super(ResPartnerGenre, self).write(values)
        ref = str(self.genre) + ' ' + str(self.zip) + ' ' + str(self.lang)
        print(ref)
        self.env.cr.execute(""" UPDATE res_partner SET ref = '{}' where id = {}""".format(ref, self.id))
        return res