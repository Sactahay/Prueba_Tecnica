# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResearchProject(models.Model):
    _name = 'research.project'
    _description = 'Proyecto de Investigación'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre del Proyecto', required=True)
    code = fields.Char(string='Código del Proyecto', default=lambda self: self.env['ir.sequence'].next_by_code('research.project.sequence') or 'Nuevo')
    description = fields.Text(string='Descripción del Proyecto')
    start_date = fields.Date(string='Fecha de Inicio', default=fields.Date.today)
    end_date = fields.Date(string='Fecha Estimada de Finalización')
    budget = fields.Float(string='Presupuesto Asignado')
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_progreso', 'En Progreso'),
        ('en_revision', 'En Revisión'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ], string='Estado del Proyecto', default='nuevo', tracking=True)
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    ], string='Prioridad', default='1', index=True, tracking=True)
    investigator_ids = fields.Many2many('res.partner', string='Investigadores Participantes')
    leader_id = fields.Many2one('res.partner', string='Investigador Principal', domain="[('is_company', '=', False)]")
    progress = fields.Float(string='Progreso (%)', compute='_compute_progress', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_progress(self):
        for record in self:
            if record.start_date and record.end_date:
                today = fields.Date.today()
                if record.start_date <= today <= record.end_date:
                    difference = (record.end_date - record.start_date).days
                    elapsed = (today - record.start_date).days
                    record.progress = (elapsed / difference) * 100 if difference > 0 else 0.0
                elif today > record.end_date:
                    record.progress = 100.0
                else:
                    record.progress = 0.0
            else:
                record.progress = 0.0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.start_date > record.end_date:
                raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de finalización.")

    @api.onchange('leader_id')
    def _onchange_leader_id(self):
        if self.leader_id and self.leader_id not in self.investigator_ids:
            return {
                'warning': {
                    'title': "Advertencia",
                    'message': "El investigador principal no está incluido en la lista de investigadores participantes. ¿Desea agregarlo?",
                },
                'value': {'investigator_ids': [(4, self.leader_id.id)]}
            }

    def action_en_progreso(self):
        self.write({'state': 'en_progreso'})

    def action_en_revision(self):
        self.write({'state': 'en_revision'})

    def action_completado(self):
        self.write({'state': 'completado'})

    def action_cancelado(self):
        self.write({'state': 'cancelado'})

    def action_nuevo(self):
        self.write({'state': 'nuevo'})