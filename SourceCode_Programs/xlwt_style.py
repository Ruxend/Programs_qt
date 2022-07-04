#!/usr/bin/env python 
#coding=utf-8 
import xlwt

class main():
	def font(self):
		"""
		设置字体样式
		"""
		# 可设置项########################################################
		# self.height = 0x00C8  # 200: this is font with height 10 points
		# self.italic = False
		# self.struck_out = False
		# self.outline = False  # 设置轮廓
		# self.shadow = False 	# 设置阴影
		# self.colour_index = 0x7FFF
		# self.bold = False
		# self._weight = 0x0190  # 0x02BC gives bold font
		# self.escapement = self.ESCAPEMENT_NONE 	# 设置字体上下标、上标
		# self.underline = self.UNDERLINE_NONE
		# self.family = self.FAMILY_NONE
		# self.charset = self.CHARSET_SYS_DEFAULT
		# self.name = "Arial"
		# ESCAPEMENT_NONE         = 0x00
		# 上下标索引###############################################
		# # 上标
		# ESCAPEMENT_SUPERSCRIPT  = 0x01
		# # 下标
		# ESCAPEMENT_SUBSCRIPT    = 0x02
		# # 下划线可选值
		# UNDERLINE_NONE          = 0x00
		# UNDERLINE_SINGLE        = 0x01
		# UNDERLINE_SINGLE_ACC    = 0x21
		# UNDERLINE_DOUBLE        = 0x02
		# UNDERLINE_DOUBLE_ACC    = 0x22
		font = xlwt.Font() 					# Create Font
		font.name = "Arial Narrow"			# 类型
		font.colour_index = 0 				# 颜色
		font.height = 10*20 				# 字号*20
		font.bold = False 					# 是否加粗
		font.underline = False 				# 下划线
		font.italic = False 				# 斜体
		font.struck_out = False 			# 删除线
		return font

	def borders(self):
		"""
		设置边框样式
		"""
		borders = xlwt.Borders() 			# Create Borders
		# May be:   NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
		#		   MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
		#		   MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
		# DASHED虚线
		# NO_LINE没有
		# THIN实线
		# 边框线型索引######################################################
		# NO_LINE = 0x00
		# THIN    = 0x01
		# MEDIUM  = 0x02
		# DASHED  = 0x03
		# DOTTED  = 0x04
		# THICK   = 0x05
		# DOUBLE  = 0x06
		# HAIR    = 0x07
		# #The following for BIFF8
		# MEDIUM_DASHED               = 0x08
		# THIN_DASH_DOTTED            = 0x09
		# MEDIUM_DASH_DOTTED          = 0x0A
		# THIN_DASH_DOT_DOTTED        = 0x0B
		# MEDIUM_DASH_DOT_DOTTED      = 0x0C
		# SLANTED_MEDIUM_DASH_DOTTED  = 0x0D
		# 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
		# 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
		# 可设置项(默认值)######################################################
		# self.left = self.NO_LINE
		# self.right = self.NO_LINE
		# self.top = self.NO_LINE
		# self.bottom = self.NO_LINE
		# self.diag = self.NO_LINE

		# self.left_colour = 0x40
		# self.right_colour = 0x40
		# self.top_colour = 0x40
		# self.bottom_colour = 0x40
		# self.diag_colour = 0x40 		# 内边框 粗线

		# self.need_diag1 = self.NO_NEED_DIAG1
		# self.need_diag2 = self.NO_NEED_DIAG2

		borders.left = xlwt.Borders.THIN
		borders.right = xlwt.Borders.THIN
		borders.top = xlwt.Borders.THIN
		borders.bottom = xlwt.Borders.THIN
		borders.left_colour = xlwt.Style.colour_map["black"]
		borders.right_colour = xlwt.Style.colour_map["black"]
		borders.top_colour = xlwt.Style.colour_map["black"]
		borders.bottom_colour = xlwt.Style.colour_map["black"]
		return borders

	def pattern(self):
		"""
		设置单元格背景色
		"""
		pattern = xlwt.Pattern() 			# Create Pattern
		# 可设置项(默认值)###################################################
		# self.pattern = self.NO_PATTERN 	# 打开/关闭填充
		# self.pattern_fore_colour = 0x40 	# 填充前景色
		# self.pattern_back_colour = 0x14 	# 填充背景色

		# May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
		pattern.pattern = xlwt.Pattern.NO_PATTERN 						# 设置背景颜色模式
		# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow,
		# 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
		# almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
		# pattern.pattern_fore_colour = xlwt.Style.colour_map["black"] 		# 设置背景颜色
		return pattern

	def alig(self):
		"""
		设置对齐样式
		"""
		alig = xlwt.Alignment() 			# Create Alignment
		# VERT_TOP = 0x00	   上端对齐
		# VERT_CENTER = 0x01	居中对齐（垂直方向上）
		# VERT_BOTTOM = 0x02	低端对齐
		# HORZ_LEFT = 0x01	  左端对齐
		# HORZ_CENTER = 0x02	居中对齐（水平方向上）
		# HORZ_RIGHT = 0x03	 右端对齐
		# 可设置项(默认值)#####################################################
		# self.horz = self.HORZ_GENERAL
		# self.vert = self.VERT_BOTTOM
		# self.dire = self.DIRECTION_GENERAL
		# self.orie = self.ORIENTATION_NOT_ROTATED
		# self.rota = self.ROTATION_0_ANGLE 	# 旋转方向，设置旋转方向
		# self.wrap = self.NOT_WRAP_AT_RIGHT
		# self.shri = self.NOT_SHRINK_TO_FIT 	# 自动缩进设置
		# self.inde = 0
		# self.merg = 0
		# 其他对齐方式索引#####################################################
		# 水平对齐方式
		# HORZ_GENERAL                = 0x00
		# HORZ_LEFT                   = 0x01
		# HORZ_CENTER                 = 0x02
		# HORZ_RIGHT                  = 0x03
		# HORZ_FILLED                 = 0x04
		# HORZ_JUSTIFIED              = 0x05 # BIFF4-BIFF8X
		# HORZ_CENTER_ACROSS_SEL      = 0x06 # Centred across selection (BIFF4-BIFF8X)
		# HORZ_DISTRIBUTED            = 0x07 # Distributed (BIFF8X)
		# # 垂直对齐方式
		# VERT_TOP                    = 0x00
		# VERT_CENTER                 = 0x01
		# VERT_BOTTOM                 = 0x02
		# VERT_JUSTIFIED              = 0x03 # Justified (BIFF5-BIFF8X)
		# VERT_DISTRIBUTED            = 0x04 # Distributed (BIFF8X)
		# # 旋转角度
		# ROTATION_0_ANGLE            = 0x00
		# ROTATION_STACKED            = 0xFF
		# # 自动缩进设置
		# SHRINK_TO_FIT               = 0x01
		# NOT_SHRINK_TO_FIT           = 0x00
		alig.horz = xlwt.Alignment.HORZ_LEFT 	# 设置水平左端对齐
		alig.vert = xlwt.Alignment.VERT_CENTER 	# 设置垂直居中
		alig.wrap = False 						# 自动换行
		return alig

	def prot(self):
		"""
		设置单元格保护
		"""
		prot = xlwt.Protection()
		# 可设置项(默认值)########################################################
		# self.cell_locked = 1
		# self.formula_hidden = 0
		prot.cell_locked = False 			# 设置单元格锁定
		prot.formula_hidden = False 		# 设定隐藏单元格内公式
		# work_sheet.set_protect(True) 		# 只有在sheet表设置为保护时才有效
		return prot

	def style(self):
		"""
		风格样式初始化
		"""
		style = xlwt.XFStyle()					# Create Style
		style.num_format_str = "general"		# 数据格式
		# 单元格数据类型  #######################################################
		"""
			"general",
			"0",
			"0.00",
			"#,##0",
			"#,##0.00",
			""$"#,##0_);("$"#,##0)",
			""$"#,##0_);[Red]("$"#,##0)",
			""$"#,##0.00_);("$"#,##0.00)",
			""$"#,##0.00_);[Red]("$"#,##0.00)",
			"0%",
			"0.00%",
			"0.00E+00",
			"# ?/?",
			"# ??/??",
			"M/D/YY",
			"D-MMM-YY",
			"D-MMM",
			"MMM-YY",
			"h:mm AM/PM",
			"h:mm:ss AM/PM",
			"h:mm",
			"h:mm:ss",
			"M/D/YY h:mm",
			"_(#,##0_);(#,##0)",
			"_(#,##0_);[Red](#,##0)",
			"_(#,##0.00_);(#,##0.00)",
			"_(#,##0.00_);[Red](#,##0.00)",
			"_("$"* #,##0_);_("$"* (#,##0);_("$"* "-"_);_(@_)",
			"_(* #,##0_);_(* (#,##0);_(* "-"_);_(@_)",
			"_("$"* #,##0.00_);_("$"* (#,##0.00);_("$"* "-"??_);_(@_)",
			"_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)",
			"mm:ss",
			"[h]:mm:ss",
			"mm:ss.0",
			"##0.0E+0",
			"@"
		"""
		"""
		添加样式
		"""
		style.font = self.font() 				# Add Font to Style
		style.borders = self.borders() 			# Add Borders to Style
		style.pattern = self.pattern() 			# Add Pattern to Style
		style.alignment = self.alig() 			# Add Alignment to Style
		style.protection = self.prot() 			# Add Protection to Style
		return style


style = main().style()
# if __name__ == "__main__":



