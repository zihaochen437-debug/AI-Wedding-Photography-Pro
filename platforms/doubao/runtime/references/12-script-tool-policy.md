# 豆包脚本与工具政策

豆包版开放 Python、Node、Shell、PowerShell、Batch、命令行工具、FFmpeg、ImageMagick 等辅助能力，但**运行状态必须真实验证**。

## 推荐职责

- `project_init.py`：项目目录与状态快照
- `asset_registry.py`：资产 ID/版本/父子关系/状态
- `reference_manifest.py`：参考归属、评级、职责和是否可进入生成输入
- `output_size_calculator.py`：按运行时实际比例/长边计算尺寸，不假设固定 8000×12000
- `asset_board_layout.py`：原子资产非生成式排版、中文标签、版本/状态
- `batch_planner.py`：照片/视频执行批次规划
- `prompt_manifest.py`：保存实际 Prompt、模型、参考绑定和参数
- `shot_list_export.py`：导出 Scene→Look→Sequence→Shot 清单
- `timeline_validator.py`：验证视频时间轴连续/无重叠
- `media_processor.py`：在 FFmpeg 实际存在时抽帧/转码/拼接/音频/封装
- `qc_report_generator.py`：汇总 QC；语义身份判断由 Agent/视觉模型完成
- `runtime_probe.py`：探测 Python/FFmpeg/ImageMagick/Pillow 等实际状态
- `package_validator.py`：结构、YAML/JSON、脚本语法、Active Canon 实现目标和密钥扫描

## 禁止

脚本不得自动决定瘦脸、年龄、民族、疾病/残障、身体改造、个人特征删除、用户批准或“是否更漂亮”；不得静默上传真人资料、嵌入密钥、绕过审批、自动安装无关程序。

## 回退

脚本依赖不可用时标记 `SCRIPT_CALLABLE = UNKNOWN/UNSUPPORTED` 并回退到 Agent/用户可执行方案，不伪造已完成。
